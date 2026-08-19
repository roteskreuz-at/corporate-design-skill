# ÖRK-CD-Skill für Claude

Ein [Agent Skill](https://code.claude.com/docs/en/skills) für Claude Code und
Claude-Apps: das Corporate Design des Österreichischen Roten Kreuzes —
Auskunft, Materialerzeugung und CD-Prüfung. Inklusive Landesverbände und
Jugendrotkreuz.

**Kein offizielles Produkt des ÖRK.** Alle Inhalte sind maschinell aus dem
offiziellen Styleguide design.roteskreuz.at (63 Seiten, erhoben 2026-08-19) und
den dort hinterlegten Dateien extrahiert und **nicht fachlich freigegeben**.
Verbindliche Auskünfte gibt cd@roteskreuz.at.

## Was der Skill kann

1. **Auskunft:** CD-Fragen präzise beantworten — Farben (alle fünf Farbsysteme),
   Logo (Schutzzone, Mindestgrößen, Verbote), Typografie, Gestaltungsraster,
   Emblemrecht, Markenkommunikation, Digital/Print/Branding/Audio, JRK.
2. **Erzeugen:** Dokumente, Präsentationen, Grafiken, Web- und Social-Media-
   Material im ÖRK-CD — mit korrekten Werten aus den Design-Tokens statt aus
   (nachweislich fehlerhaften) Bestandsvorlagen.
3. **Prüfen:** Dateien gegen die Token-Sollwerte abgleichen, inklusive der
   bekannten Fehlermuster aus der Bestandsauswertung 2026.

Eingebaute Leitplanken: Das rote Kreuz wird niemals generiert oder nachgebaut
(Rotkreuzgesetz!), nur Original-Logodateien werden eingesetzt; die
ÖRK-KI-Richtlinie (Kennzeichnungspflicht) wird mitgeführt.

## Installation

```bash
git clone <repo-url> ~/.claude/skills/oerk-cd
```

Mehr braucht es nicht — Claude Code lädt Skills aus `~/.claude/skills/`
automatisch. Optional: Hausschrift Dunant lokal installieren (Download über
design.roteskreuz.at, Lizenz beachten); ohne sie verwendet der Skill die
offiziellen Ersatzschriften Arial/Helvetica.

## Aufbau

| Pfad | Inhalt |
|---|---|
| `SKILL.md` | Einstieg: Kernwerte, Leitplanken, Arbeitsablauf |
| `references/` | 13 destillierte Referenzen (Farben, Logo, Emblemrecht, …) |
| `data/` | Maschinenlesbare Quelle: W3C-Design-Tokens, Regeln, Domains, Schemas |
| `assets/logos/` | ÖRK-Basislogo, Sonderlogo, ÖJRK-Logo (deutsch) |
| `assets/dist/` | Office-Theme, Adobe-ASE, CSS — aus den Tokens gebaut |
| `quellen/portal/` | Rohtext aller 63 Portalseiten (Erhebung 2026-08-19) |
| `tools/` | `validate.py` (Datenprüfung), `build.py` (dist neu bauen), `crawl_portal.py` (Portal neu erheben) |

## Pflege

1. Portal neu erheben: `python3 tools/crawl_portal.py /tmp/portal-scrape`, dann
   `text/*.md` gegen `quellen/portal/` diffen und übernehmen sowie
   `seiten-index.json` nach `quellen/` kopieren
2. Werte ändern nur in `data/tokens/`, dann `python3 tools/validate.py` (0 Fehler)
   und `python3 tools/build.py`
3. Referenzen unter `references/` nachziehen

## Rechtliches

Das Rotkreuzzeichen ist völkerrechtlich geschützt (Genfer Abkommen,
Rotkreuzgesetz); Logos und Portalinhalte gehören dem Österreichischen Roten
Kreuz. Dieses Repository ist für die Arbeit im und für das ÖRK gedacht — keine
Verwendung der Marken- und Bildbestandteile außerhalb dieses Rahmens.
