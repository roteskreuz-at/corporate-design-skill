#!/usr/bin/env python3
"""
Qualitaetssicherung fuer die ÖRK-CD-Quelle.

Laeuft bei jedem Commit. Faehrt mit Exit-Code 1 heraus, wenn ein FEHLER auftritt –
damit bricht der Build ab und eine kaputte Quelle wird nicht ausgeliefert.
Genau das hat in der Vorgaengerversion gefehlt: dort lagen Schemas bei, es hat sie
aber nie jemand ausgefuehrt, und eine der fuenf Dateien war schlicht ungueltig.

Aufruf:   python tools/validate.py [--strict]
          --strict behandelt zusaetzlich WARNUNGEN als Fehler.

Benoetigt: pip install jsonschema
"""

import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

try:
    from jsonschema import Draft7Validator, FormatChecker
except ImportError:
    print("FEHLER: 'jsonschema' fehlt.  ->  pip install jsonschema")
    sys.exit(1)

WURZEL = Path(__file__).resolve().parent.parent / "data"
RECORD_ORDNER = ["rules", "domains", "registry"]
TOKEN_ORDNER = "tokens"

fehler, warnungen, hinweise = [], [], []


def f(msg):  fehler.append(msg)
def w(msg):  warnungen.append(msg)
def h(msg):  hinweise.append(msg)


def lade(pfad: Path):
    try:
        return json.loads(pfad.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        f(f"{pfad.relative_to(WURZEL)}: kein gueltiges JSON – {e}")
        return None


# ---------------------------------------------------------------- 1. Schemas
def pruefe_schemata():
    record_schema = lade(WURZEL / "schema" / "record.schema.json")
    manifest_schema = lade(WURZEL / "schema" / "manifest.schema.json")
    if not record_schema or not manifest_schema:
        return None

    manifest = lade(WURZEL / "manifest.json")
    if manifest:
        v = Draft7Validator(manifest_schema, format_checker=FormatChecker())
        for e in v.iter_errors(manifest):
            f(f"manifest.json{list(e.absolute_path)}: {e.message}")

    v = Draft7Validator(record_schema, format_checker=FormatChecker())
    for ordner in RECORD_ORDNER:
        for pfad in sorted((WURZEL / ordner).glob("*.json")):
            daten = lade(pfad)
            if daten is None:
                continue
            for e in v.iter_errors(daten):
                f(f"{pfad.relative_to(WURZEL)}{list(e.absolute_path)}: {e.message}")
    return manifest


# ------------------------------------------------- 2. Manifest <-> Dateisystem
def pruefe_vollstaendigkeit(manifest):
    if not manifest:
        return
    gelistet = set()
    for eintrag in manifest.get("eintraege", []):
        rel = eintrag["datei"]
        gelistet.add(rel)
        if not (WURZEL / rel).exists():
            f(f"manifest.json listet '{rel}' – Datei existiert nicht.")

    vorhanden = set()
    for ordner in RECORD_ORDNER + [TOKEN_ORDNER]:
        for pfad in (WURZEL / ordner).glob("*.json"):
            vorhanden.add(pfad.relative_to(WURZEL).as_posix())

    for rel in sorted(vorhanden - gelistet):
        f(f"'{rel}' liegt im Paket, ist aber nicht im Manifest gelistet.")


# --------------------------------------------- 3. Sichtbarkeit / Datenschutz
def kopf(daten: dict) -> dict:
    """Datensatzkopf holen. Token-Dateien folgen dem DTCG-Format und duerfen
    keine Fremdfelder auf oberster Ebene fuehren – ihr Kopf liegt daher unter
    $extensions."""
    if "sichtbarkeit" in daten:
        return daten
    return daten.get("$extensions", {}).get("at.roteskreuz.cd", {}).get("record", {})


def pruefe_sichtbarkeit(manifest):
    if not manifest:
        return
    for eintrag in manifest.get("eintraege", []):
        pfad = WURZEL / eintrag["datei"]
        if not pfad.exists():
            continue
        rohdaten = lade(pfad)
        if not rohdaten:
            continue
        daten = kopf(rohdaten)
        if daten.get("sichtbarkeit") != eintrag.get("sichtbarkeit"):
            f(f"{eintrag['datei']}: sichtbarkeit im Datensatz "
              f"('{daten.get('sichtbarkeit')}') weicht vom Manifest "
              f"('{eintrag.get('sichtbarkeit')}') ab.")
        if rohdaten.get("datenschutz", {}).get("enthaelt_personenbezogene_daten") \
                and daten.get("sichtbarkeit") == "oeffentlich":
            f(f"{eintrag['datei']}: enthaelt personenbezogene Daten, ist aber "
              f"als oeffentlich markiert. Das darf der Build nie ausliefern.")


# ------------------------------------------------ 4. Token-Referenzen (DTCG)
REF = re.compile(r"^\{([^}]+)\}$")


def sammle_tokens(knoten, pfad, ziel):
    if isinstance(knoten, dict):
        if "$value" in knoten:
            ziel[".".join(pfad)] = knoten
            return
        for schluessel, wert in knoten.items():
            if schluessel.startswith("$"):
                continue
            sammle_tokens(wert, pfad + [schluessel], ziel)


def finde_referenzen(wert):
    if isinstance(wert, str):
        m = REF.match(wert.strip())
        return [m.group(1)] if m else []
    if isinstance(wert, dict):
        out = []
        for v in wert.values():
            out += finde_referenzen(v)
        return out
    if isinstance(wert, list):
        out = []
        for v in wert:
            out += finde_referenzen(v)
        return out
    return []


def pruefe_tokens():
    alle = {}
    for pfad in sorted((WURZEL / TOKEN_ORDNER).glob("*.tokens.json")):
        daten = lade(pfad)
        if not daten:
            continue
        lokal = {}
        sammle_tokens(daten, [], lokal)
        for name, tok in lokal.items():
            alle[name] = (pfad.name, tok)

    for name, (datei, tok) in alle.items():
        for ref in finde_referenzen(tok["$value"]):
            if ref not in alle:
                f(f"{datei}: Token '{name}' verweist auf '{{{ref}}}' – Ziel existiert nicht.")

    # Farb-Kollisionen: fast identische Werte sind fast immer ein Uebertragungsfehler
    farben = {}
    for name, (datei, tok) in alle.items():
        wert = tok["$value"]
        if isinstance(wert, dict) and "hex" in wert:
            farben[name] = (wert["hex"].upper().lstrip("#"), datei)

    namen = sorted(farben)
    for i, a in enumerate(namen):
        for b in namen[i + 1:]:
            ha, _ = farben[a]
            hb, _ = farben[b]
            if ha == hb:
                continue
            try:
                da = [abs(int(ha[k:k + 2], 16) - int(hb[k:k + 2], 16)) for k in (0, 2, 4)]
            except ValueError:
                continue
            if max(da) <= 4:
                f(f"Farbkollision: '{a}' (#{ha}) und '{b}' (#{hb}) unterscheiden sich um "
                  f"maximal {max(da)}/255. Das ist kein Gestaltungsentscheid, sondern ein "
                  f"Uebertragungsfehler – einen kanonischen Wert festlegen.")

    # offen markierte Konflikte melden
    for pfad in sorted((WURZEL / TOKEN_ORDNER).glob("*.tokens.json")):
        daten = lade(pfad) or {}
        ext = daten.get("$extensions", {}).get("at.roteskreuz.cd", {})
        for schluessel in ("konflikt_primaerrot", "widerspruch_logorot", "kanalregel_logorot"):
            konflikt = ext.get(schluessel)
            if konflikt and konflikt.get("status") == "ungeklaert":
                w(f"{pfad.name}: '{schluessel}' ist als ungeklaert markiert. "
                  f"Bis zur Klaerung gilt die restriktivere Auslegung.")


# ------------------------------------------------------- 5. Governance / Pflege
def pruefe_governance():
    heute = date.today()
    for ordner in RECORD_ORDNER:
        for pfad in sorted((WURZEL / ordner).glob("*.json")):
            daten = lade(pfad)
            if not daten:
                continue
            rel = pfad.relative_to(WURZEL).as_posix()
            g = daten.get("governance", {})
            p = daten.get("provenance", {})

            if not p.get("human_verified", False):
                w(f"{rel}: human_verified = false – Inhalt ist maschinell extrahiert "
                  f"und fachlich noch nicht freigegeben.")

            geprueft = g.get("geprueft_am")
            if not geprueft:
                w(f"{rel}: nie fachlich geprueft (geprueft_am ist leer).")
            else:
                try:
                    faellig = date.fromisoformat(geprueft) + timedelta(
                        days=30 * int(g.get("review_intervall_monate", 12)))
                    if faellig < heute:
                        f(f"{rel}: Review ueberfaellig seit {faellig.isoformat()}.")
                except ValueError:
                    f(f"{rel}: geprueft_am ist kein gueltiges Datum ('{geprueft}').")

            owner = g.get("owner", "")
            if owner and not owner.split("@")[0].isalpha():
                h(f"{rel}: owner '{owner}' sieht nach Person aus – Rollenpostfach verwenden.")

            for op in daten.get("offene_punkte", []):
                h(f"{rel}: offen – {op['frage']}")


# ------------------------------------------------------------------ 6. Bericht
def main():
    strict = "--strict" in sys.argv

    manifest = pruefe_schemata()
    pruefe_vollstaendigkeit(manifest)
    pruefe_sichtbarkeit(manifest)
    pruefe_tokens()
    pruefe_governance()

    print("=" * 74)
    print("ÖRK CD – Qualitaetssicherung")
    print("=" * 74)

    for titel, liste, zeichen in (("FEHLER", fehler, "x"),
                                  ("WARNUNGEN", warnungen, "!"),
                                  ("OFFENE PUNKTE", hinweise, "-")):
        print(f"\n{titel} ({len(liste)})")
        if not liste:
            print("  keine")
        for eintrag in liste:
            print(f"  {zeichen} {eintrag}")

    print("\n" + "=" * 74)
    if fehler:
        print(f"ERGEBNIS: FEHLGESCHLAGEN – {len(fehler)} Fehler. Build wird abgebrochen.")
        return 1
    if strict and warnungen:
        print(f"ERGEBNIS: FEHLGESCHLAGEN (--strict) – {len(warnungen)} Warnungen.")
        return 1
    print(f"ERGEBNIS: BESTANDEN – 0 Fehler, {len(warnungen)} Warnungen, "
          f"{len(hinweise)} offene Punkte.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
