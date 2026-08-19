---
name: oerk-cd
description: >-
  Corporate Design des Österreichischen Roten Kreuzes (ÖRK) inkl. Landesverbände und
  Jugendrotkreuz. Anwenden bei: (1) Fragen zum ÖRK-CD — Farben, Logo, Schrift,
  Gestaltungsraster, Vorlagen, design.roteskreuz.at; (2) Erzeugen von Material mit
  ÖRK-/Rotkreuz-Bezug — Dokumente, Präsentationen, Grafiken, Social Media, Web, E-Mail;
  (3) Fragen zum Rotkreuzzeichen und Emblemrecht (wer darf ein rotes Kreuz verwenden);
  (4) Prüfen von Dateien gegen das ÖRK-CD. Auch bei anderen Rotkreuz-Gesellschaften
  (IKRK, IFRC, DRK …) laden — dort nur zur Abgrenzung, nicht als deren Regelwerk.
---

# ÖRK Corporate Design

Verbindliche Werte und Regeln des Österreichischen Roten Kreuzes, destilliert aus dem
vollständigen Styleguide design.roteskreuz.at (63 Seiten, erhoben 2026-08-19) und den
maschinenlesbaren Datensätzen unter `data/`. Kein Inhalt ist vom ÖRK fachlich
freigegeben — bei Erstnutzung in einer Session einmal darauf hinweisen.

## Harte Leitplanken (gehen allem voran)

1. **Das rote Kreuz niemals generieren, nachzeichnen, verfremden oder aus Formen
   nachbauen** — ausschließlich die Original-Logodateien einsetzen (`assets/logos/`
   oder Portal-Download). Das Rotkreuzzeichen ist völkerrechtlich geschützt; Missbrauch
   ist in Österreich strafbar (bis 15.000 €). Details: `references/emblemrecht.md` —
   bei jeder Frage, wer ein rotes Kreuz verwenden darf, zuerst diese Datei lesen.
2. **KI-Kennzeichnung:** Die ÖRK-KI-Richtlinie (Weisung) verlangt die Kennzeichnung
   von Inhalten mit Anschein von Realität sowie ungeprüft veröffentlichter Inhalte.
   Nach jedem erzeugten Deliverable den Kennzeichnungshinweis aktiv mitliefern;
   ob und wie der Vermerk ins Dokument kommt, entscheidet der Mensch — die Pflicht
   nach der Weisung bleibt bestehen (Details: `references/rechtliches.md`).
3. Erzeugte Materialien sind **Entwürfe**: Freigabe durch die zuständige Stelle
   (cd@roteskreuz.at bzw. Landesverband) liegt beim Menschen.

## Kernwerte (für jede Aufgabe)

| Wert | Regel |
|---|---|
| **Dunkelrot #B70E0C** (Pantone 1805 C) | Der Arbeitston für Gestaltung — Flächen, Schrift, Akzente. Immer 100 % Deckkraft. |
| **Logorot #FF0000** (Pantone 485 C) | Kanalregel: Print/analog NUR im Wahrzeichen. Digital zusätzlich als Zusatzfarbe max. 10 % Fläche (CTAs, Störer). |
| **Grau #838383** | Das ÖRK-Grau. Häufigster Fehler: Office-Standardgrau #808080 — nie verwenden. |
| **Schrift Dunant** | Hausschrift (Light/Regular/Medium/Bold). Wenn nicht installiert: Arial bzw. Helvetica (nie Verdana). |
| **Weiß/Schwarz** | #FFFFFF / #000000, Print s. `references/farben.md`. |

Farben und Schriften beim Erzeugen immer aus diesen Werten bzw. `data/tokens/` setzen,
nie aus Bestandsvorlagen übernehmen (deren Themes sind nachweislich fehlerhaft,
s. `references/print.md`).

## Arbeitsablauf

- **Auskunft:** Passende Referenz(en) aus der Tabelle unten lesen, Antwort mit exakten
  Werten geben. Bei unklarer oder fehlender Quellenlage das sagen — nie plausibel
  raten. Bei Widersprüchen gilt die Präzedenz `L0-recht > L1-marke > L2-anwendung >
  L3-vorlage > L4-subbrand` (Details: `data/manifest.json`). Die Präzedenz greift
  nur bei echtem Widerspruch — für JRK-Material gelten zuerst die spezifischen
  JRK-Regeln (Logo, Farben), die Basis-Ebenen füllen nur die Lücken.
- **Erzeugen:** `farben.md`, `typografie.md`, `logo.md` immer lesen, dazu die
  kanalspezifische Referenz (digital/print/…). Logos aus `assets/logos/`,
  Office-Theme und Paletten aus `assets/dist/`.
- **Prüfen:** Datei gegen `data/tokens/` abgleichen; Vorgehen und bekannte
  Fehlermuster in `references/pruefen.md`.
- **Andere Rotkreuz-Gesellschaften** (IKRK, IFRC, DRK, …): Dieses Regelwerk gilt nur
  für das ÖRK. Explizit abgrenzen; für die Föderation auf brand.ifrc.org verweisen.

## Referenzen

| Datei | Lesen bei |
|---|---|
| `references/farben.md` | jeder Farbfrage und jedem Deliverable |
| `references/typografie.md` | Schriftwahl, Textsatz, Dokumenterzeugung |
| `references/logo.md` | Logoeinsatz: Schutzzone, Mindestgrößen, Varianten, Verbote |
| `references/emblemrecht.md` | Rotkreuzzeichen, Verwendungsrecht, Schutzzeichen — höchste Präzedenz |
| `references/markenkommunikation.md` | jedem Text: Tonalität, verbindliche Schreibweisen, Claim |
| `references/bildwelt.md` | Bildauswahl, Fotografie, Bildstil |
| `references/rechtliches.md` | Bildrechte, Barrierefreiheit, KI-Regeln des ÖRK |
| `references/digital.md` | Web, E-Mail, Social Media (Formate 1:1/4:5/9:16), Banner, Konferenzen |
| `references/print.md` | Gestaltungsraster, Drucksorten, Office-Vorlagen |
| `references/branding.md` | Fahrzeuge, Uniform, Gebäude, Werbemittel |
| `references/audio-video.md` | Audio-Logo, Corporate Song, Telefonansagen, Video |
| `references/jugendrotkreuz.md` | allem mit JRK-Bezug (Sub-Brand, L4) |
| `references/pruefen.md` | Dateien gegen das CD prüfen |

## Assets im Skill

- `assets/logos/basislogo/` — ÖRK-Basislogo deutsch: RGB-PNG, CMYK/Pantone/SW-EPS
- `assets/logos/sonderlogo/` — Sonderlogo deutsch (RGB-JPG, CMYK-EPS)
- `assets/logos/jrk/` — ÖJRK-Logo überregional, mit Slogan (RGB-JPG, CMYK-EPS)
- `assets/dist/theme1.xml` — korrektes Office-Theme (aus den Tokens gebaut)
- `assets/dist/OERK-Farben.ase` — Adobe-Farbfeldbibliothek
- `assets/dist/oerk-farben.css`, `oerk-farben-flach.json` — Web-/Flachwerte

Weitere Sprachversionen, Landesverbands-Mutationen und Vorlagen: Download-URLs stehen
in den Referenzen; Quelle ist immer design.roteskreuz.at (mit Quellenangabe verwenden).
Der Rohtext aller Portalseiten liegt unter `quellen/portal/`, der Seiten- und
Dateiindex in `quellen/seiten-index.json` — dort nachsehen, wenn eine Detailfrage in
den Referenzen fehlt.
