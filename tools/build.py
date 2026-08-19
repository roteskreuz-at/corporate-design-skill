#!/usr/bin/env python3
"""
Baut aus den Design-Tokens (der One Place of Truth) alle Ausgabeformate:

  dist/theme1.xml            korrigiertes Office-Farb- und Schriftschema (OOXML)
  dist/OERK-Farben.ase       Adobe-Farbfeldbibliothek (RGB- und CMYK-Gruppe)
  dist/oerk-farben.css       CSS-Custom-Properties fuer Web/Apps
  dist/oerk-farben-flach.json  flacher Export fuer beliebige Werkzeuge

Grundprinzip: KEIN Wert steht in diesem Skript. Alle Farb- und Schriftwerte
kommen aus tokens/color.tokens.json und tokens/typography.tokens.json.
Wer eine Farbe aendern will, aendert sie dort - und baut neu.

Aufruf:  python tools/build.py
"""

import io
import json
import re
import struct
import sys
import zipfile
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent / "data"
DIST = WURZEL / "dist"

# Scaffold fuer das vollstaendige Theme (fmtScheme etc. werden uebernommen,
# clrScheme und fontScheme durch Token-Werte ersetzt): die offizielle
# PowerPoint-Vorlage 2026 vom Portal.
SCAFFOLD_POTX = (WURZEL.parent / "belege" / "originaldateien" / "fileadmin" /
                 "user_upload" / "Digitales_CD" / "Vorlagen" /
                 "PRAES_OERK_DIGITAL_PP_2026_de-en-16-9_V1_13042026.potx")


def lade_tokens():
    farbe = json.loads((WURZEL / "tokens" / "color.tokens.json").read_text(encoding="utf-8"))
    typo = json.loads((WURZEL / "tokens" / "typography.tokens.json").read_text(encoding="utf-8"))
    basis = farbe["farbe"]["basis"]

    def t(name):
        tok = basis[name]
        ext = tok.get("$extensions", {}).get("at.roteskreuz.cd", {})
        return {
            "hex": tok["$value"]["hex"].lstrip("#").upper(),
            "cmyk": ext.get("cmyk"),
            "pantone": ext.get("pantone"),
        }

    farben = {n: t(n) for n in basis if not n.startswith("$")}
    haus = typo["schrift"]["familie"]["haus"]["$value"][0]   # "Dunant"
    return farben, haus


# --------------------------------------------------------------- Office-Theme
# Rollenzuordnung: identisch mit der Absicht der offiziellen Vorlage 2026
# (dk2 = Arbeitsrot, lt2 = Grau, accent1-6 = Rotreihe dunkel->hell),
# nur mit den verbindlichen Werten laut Styleguide.
THEME_ROLLEN = {
    "dk2": "dunkelrot", "lt2": "grau",
    "accent1": "rot-95", "accent2": "rot-80", "accent3": "rot-60",
    "accent4": "rot-40", "accent5": "rot-20", "accent6": "rot-05",
    "hlink": "dunkelrot", "folHlink": "dunkelrot",
}


def patch_clrscheme(theme_xml: str, farben: dict, name: str) -> str:
    for rolle, token in THEME_ROLLEN.items():
        hexwert = farben[token]["hex"]
        theme_xml = re.sub(
            rf"(<a:{rolle}>).*?(</a:{rolle}>)",
            rf'\1<a:srgbClr val="{hexwert}"/>\2',
            theme_xml, flags=re.S)
    theme_xml = re.sub(r'(<a:clrScheme name=")[^"]*(")', rf"\g<1>{name}\2", theme_xml)
    return theme_xml


def patch_fontscheme(theme_xml: str, haus: str, name: str) -> str:
    def ersetze(block_match):
        block = block_match.group(0)
        return re.sub(r'(<a:latin typeface=")[^"]*(")', rf"\g<1>{haus}\2", block, count=1)

    theme_xml = re.sub(r"<a:majorFont>.*?</a:majorFont>", ersetze, theme_xml, flags=re.S)
    theme_xml = re.sub(r"<a:minorFont>.*?</a:minorFont>", ersetze, theme_xml, flags=re.S)
    theme_xml = re.sub(r'(<a:fontScheme name=")[^"]*(")', rf"\g<1>{name}\2", theme_xml)
    theme_xml = re.sub(r'(<a:theme [^>]*name=")[^"]*(")', rf"\g<1>{name}\2", theme_xml)
    return theme_xml


def baue_theme(farben, haus) -> str:
    z = zipfile.ZipFile(SCAFFOLD_POTX)
    xml = z.read("ppt/theme/theme1.xml").decode("utf-8")
    xml = patch_clrscheme(xml, farben, "ÖRK 2026")
    xml = patch_fontscheme(xml, haus, "ÖRK 2026")
    return xml


# --------------------------------------------------------------------- ASE
def _ase_block(typ: int, nutzdaten: bytes) -> bytes:
    return struct.pack(">HI", typ, len(nutzdaten)) + nutzdaten


def _ase_name(text: str) -> bytes:
    utf16 = (text + "\0").encode("utf-16-be")
    return struct.pack(">H", len(text) + 1) + utf16


def _ase_farbe_rgb(name: str, hexwert: str) -> bytes:
    r, g, b = (int(hexwert[i:i + 2], 16) / 255.0 for i in (0, 2, 4))
    daten = _ase_name(name) + b"RGB " + struct.pack(">fff", r, g, b) + struct.pack(">H", 0)
    return _ase_block(0x0001, daten)


def _ase_farbe_cmyk(name: str, cmyk) -> bytes:
    c, m, y, k = (v / 100.0 for v in cmyk)
    daten = _ase_name(name) + b"CMYK" + struct.pack(">ffff", c, m, y, k) + struct.pack(">H", 0)
    return _ase_block(0x0001, daten)


ASE_REIHENFOLGE = [
    ("ÖRK Logorot", "logorot"), ("ÖRK Dunkelrot", "dunkelrot"),
    ("ÖRK Schwarz", "schwarz"), ("ÖRK Weiß", "weiss"), ("ÖRK Grau", "grau"),
    ("ÖRK Dunkelblau", "dunkelblau"),
    ("ÖRK Rot 05", "rot-05"), ("ÖRK Rot 20", "rot-20"), ("ÖRK Rot 40", "rot-40"),
    ("ÖRK Rot 60", "rot-60"), ("ÖRK Rot 80", "rot-80"), ("ÖRK Rot 95", "rot-95"),
    ("ÖRK Blau hell", "blau-hell"), ("ÖRK Blau mittel", "blau-mittel"),
    ("ÖRK Grau hell", "grau-hell"), ("ÖRK Grau Fläche", "grau-flaeche"),
]


def baue_ase(farben) -> bytes:
    bloecke = []
    bloecke.append(_ase_block(0xC001, _ase_name("ÖRK RGB (Digital)")))
    for anzeigename, token in ASE_REIHENFOLGE:
        bloecke.append(_ase_farbe_rgb(anzeigename, farben[token]["hex"]))
    bloecke.append(_ase_block(0xC002, b""))
    bloecke.append(_ase_block(0xC001, _ase_name("ÖRK CMYK (Print)")))
    for anzeigename, token in ASE_REIHENFOLGE:
        cmyk = farben[token]["cmyk"]
        if cmyk:
            bloecke.append(_ase_farbe_cmyk(anzeigename + " (CMYK)", cmyk))
    bloecke.append(_ase_block(0xC002, b""))
    rumpf = b"".join(bloecke)
    return b"ASEF" + struct.pack(">HHI", 1, 0, len(bloecke)) + rumpf


# --------------------------------------------------------------------- CSS
def baue_css(farben) -> str:
    zeilen = [":root {"]
    for name, w in sorted(farben.items()):
        zeilen.append(f"  --oerk-{name}: #{w['hex']};")
    zeilen.append("}")
    kopf = ("/* ÖRK Farbwerte – automatisch erzeugt aus tokens/color.tokens.json.\n"
            "   NICHT von Hand bearbeiten; Quelle der Wahrheit sind die Tokens. */\n")
    return kopf + "\n".join(zeilen) + "\n"


def main():
    farben, haus = lade_tokens()
    DIST.mkdir(exist_ok=True)

    theme = baue_theme(farben, haus)
    (DIST / "theme1.xml").write_text(theme, encoding="utf-8")

    (DIST / "OERK-Farben.ase").write_bytes(baue_ase(farben))
    (DIST / "oerk-farben.css").write_text(baue_css(farben), encoding="utf-8")

    flach = {n: {"hex": "#" + w["hex"], "cmyk": w["cmyk"], "pantone": w["pantone"]}
             for n, w in farben.items()}
    (DIST / "oerk-farben-flach.json").write_text(
        json.dumps(flach, ensure_ascii=False, indent=1), encoding="utf-8")

    (DIST / "LIESMICH.md").write_text(
        "# ÖRK CD – erzeugte Ausgaben\n\n"
        "Alle Dateien hier sind **automatisch erzeugt** aus `../tokens/`.\n"
        "Nichts von Hand bearbeiten – Änderungen gehören in die Tokens, danach `python tools/build.py`.\n\n"
        "| Datei | Zweck |\n|---|---|\n"
        "| `theme1.xml` | Office-Farb- und Schriftschema (ÖRK 2026). Ersetzt in DOTX/POTX den Teil `*/theme/theme1.xml`. |\n"
        "| `OERK-Farben.ase` | Farbfeldbibliothek für InDesign/Illustrator/Photoshop – Fenster → Farbfelder → Farbfelder laden. Gruppen: RGB (Digital) und CMYK (Print). |\n"
        "| `oerk-farben.css` | CSS-Custom-Properties für Web und Apps. |\n"
        "| `oerk-farben-flach.json` | Flacher Export für beliebige Werkzeuge. |\n\n"
        "Status: maschinell erzeugt, `human_verified: false` – vor produktivem Einsatz "
        "fachlich freigeben (cd@roteskreuz.at) und in Office/Adobe real testen.\n",
        encoding="utf-8")

    print(f"Theme:  {len(theme)} Zeichen, Rollen: {', '.join(THEME_ROLLEN)}")
    print(f"ASE:    {(DIST/'OERK-Farben.ase').stat().st_size} Bytes")
    print(f"CSS:    {len(farben)} Variablen")
    print(f"Ziel:   {DIST}")


if __name__ == "__main__":
    sys.exit(main())
