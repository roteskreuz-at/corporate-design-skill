# ÖRK CD – erzeugte Ausgaben

Alle Dateien hier sind **automatisch erzeugt** aus `data/tokens/` (Repo-Wurzel).
Nichts von Hand bearbeiten – Änderungen gehören in die Tokens, danach `python tools/build.py`.

| Datei | Zweck |
|---|---|
| `theme1.xml` | Office-Farb- und Schriftschema (ÖRK 2026). Ersetzt in DOTX/POTX den Teil `*/theme/theme1.xml`. |
| `OERK-Farben.ase` | Farbfeldbibliothek für InDesign/Illustrator/Photoshop – Fenster → Farbfelder → Farbfelder laden. Gruppen: RGB (Digital) und CMYK (Print). |
| `oerk-farben.css` | CSS-Custom-Properties für Web und Apps. |
| `oerk-farben-flach.json` | Flacher Export für beliebige Werkzeuge. |

Status: maschinell erzeugt, `human_verified: false` – vor produktivem Einsatz fachlich freigeben (cd@roteskreuz.at) und in Office/Adobe real testen.
