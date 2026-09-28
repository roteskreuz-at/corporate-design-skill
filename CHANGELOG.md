# Änderungsprotokoll

Fachliche Änderungen am Regelwerk, neueste zuerst. Technische Details stehen in
der Git-Historie; hier steht, **was sich inhaltlich geändert hat und warum** —
insbesondere jede fachlich bestätigte Korrektur durch das ÖRK.

## 2026-09-28

- **Lila-Akzentfarbe: CMYK 40|65|0|0** — erste fachlich bestätigte Korrektur im
  Datensatz (U. Freisl, GS Marketing). Der Wert 40|65|0|100 aus dem
  Akzentfarben-PDF war ein Tippfehler; das Portal-PDF führt ihn Stand
  28.09.2026 noch, die Korrektur der Designseite ist angekündigt.
  Geändert in `references/farben.md` und `data/tokens/color.tokens.json`.
- Fragenkatalog (19 offene Punkte) an die CD-Verantwortliche im GS übergeben —
  der fachliche Freigabeprozess hat damit begonnen.

## 2026-09-08

- README: Verweis auf das Schwesterprojekt
  [icons-skill](https://github.com/roteskreuz-at/icons-skill).

## 2026-08-19

- **Veröffentlichung** als `roteskreuz-at/corporate-design-skill` (öffentlich);
  zuvor DSGVO-Bereinigung: personenbezogene Ansprechpartner-Daten aus den
  gespiegelten Portaltexten entfernt, Funktionspostfächer belassen.
- `ANLEITUNG.md`: Einbindung in Claude, ChatGPT, Codex, Gemini, Copilot,
  Cursor, M365 Copilot sowie Nutzung ohne KI.
- **Review-Fixes** (zwei unabhängige KI-Reviews, Codex + Antigravity):
  Farbrollen-Korrektur im Office-Theme (fehlerhaftes Rot sitzt in `dk2`, nicht
  `accent1`), Logorot als Kanalregel statt „ungeklärt" in den Tokens
  (Print: nur Wahrzeichen; digital: Zusatzfarbe bis 10 %), CTA-Token auf
  Dunkelrot, 10 Akzentfarben in die Tokens aufgenommen, `build.py` lauffähig
  gemacht (Pfade, eingechecktes Theme-Gerüst).
- **Erstfassung:** 13 Referenzen aus dem vollständigen Styleguide
  design.roteskreuz.at (63 Seiten, erhoben 19.08.2026), W3C-Design-Tokens,
  Regeln mit Präzedenzmodell (L0-recht bis L4-subbrand), kuratierte Logos,
  Office-Theme/ASE/CSS, Portal-Rohtexte, Werkzeuge (validate/build/crawl).
  Kein Inhalt fachlich freigegeben (`human_verified: false`).
