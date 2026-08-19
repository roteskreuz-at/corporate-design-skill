# Dateien gegen das ÖRK-CD prüfen

> Quellen: data/registry/vorlagen-befund.json, data/tokens/, Auswertung aller 294 Portaldateien (2026-08-04) · Stand: 2026-08-19
> Verbindlichkeit: empfehlung (Prüfmethodik) · Fachlich freigegeben: nein

Vorgehen, um Office-, InDesign- oder Web-Dateien auf CD-Konformität zu prüfen.
Sollwerte kommen immer aus `data/tokens/` — nie aus einer anderen Datei ableiten.

## Prüfschritte Office-Dateien (docx/pptx/xlsx)

OOXML-Dateien sind ZIP-Archive. Entpacken und prüfen:

1. **Farbschema** (`ppt/theme/theme1.xml` bzw. `word/theme/theme1.xml`):
   `<a:accent1>` muss `B70E0C` führen. Sollwerte der ganzen Palette:
   `assets/dist/theme1.xml` (aus den Tokens gebaut) direkt vergleichen.
2. **Schriftschema** (`<a:majorFont>`/`<a:minorFont>` im Theme): muss `Dunant`
   führen, nicht Calibri/Cambria/Aptos.
3. **Hart codierte Farben** in Slides/Dokumenttext: nach bekannten Fehlwerten
   greppen (Liste unten).
4. **Schriften im Fließtext**: `grep -o 'typeface="[^"]*"'` — fremde Schriften melden.

```bash
unzip -o datei.pptx -d entpackt/
grep -o '<a:srgbClr val="[0-9A-Fa-f]*"' -r entpackt/ | sort | uniq -c | sort -rn
```

## Bekannte Fehlermuster (aus der Auswertung 2026-08)

| Fehlwert | Richtig | Typischer Fundort |
|---|---|---|
| `808080` (Office-Grau) | `838383` | überall — 16-mal häufiger als der richtige Wert |
| `B70F0B`, `B70E0B` | `B70E0C` | POTX-Theme accent1, hart codierte Hintergründe |
| `D46D6E` | `D46E6E` | Rotabstufung im Theme |
| `C33C3C` | `C43D3D` | Rotabstufung im Theme |
| `89090A` | `8A0A0A` | Rotabstufung im Theme |
| `5B0804` | `5C0805` | Rotabstufung im Theme |
| Calibri/Cambria/Aptos im Schriftschema | Dunant | 57 von 65 geprüften Office-Dateien |
| Microsoft-Standardtheme 2007/2016 | ÖRK-Theme | 12 JRK-DOTX + 3 Namensschild-Vorlagen |
| Schriftschnitt „Dunant School" | ungeklärt | 47 von 49 JRK-InDesign-Vorlagen |

Toleranzregel der Farbkollisionsprüfung: Farben, die sich je Kanal um ≤ 4/255 vom
Sollwert unterscheiden, sind fast immer Tippfehler-Varianten des Sollwerts — melden.

## InDesign/EPS/PDF

Nur Metadaten-Prüfung möglich (XMP): verwendete Schriften und benannte Farbfelder
auslesen. Bekanntes Problem: dieselbe Farbe trägt in Bestandsvorlagen bis zu drei
verschiedene Farbfeld-Namen — Namen gegen `data/tokens/color.tokens.json` prüfen.

## Web/CSS

Ist-Werte gegen `assets/dist/oerk-farben.css` bzw. `oerk-farben-flach.json` diffen.

## Werkzeuge im Repo

- `tools/validate.py` — prüft die Datenbestände unter `data/` selbst (Schema,
  Token-Referenzen, Farbkollisionen): `python3 tools/validate.py`
- `tools/build.py` — erzeugt `assets/dist/` (Office-Theme, ASE, CSS) neu aus den
  Tokens: `python3 tools/build.py`

Nach jeder Korrektur an den Tokens: erst `validate.py` (0 Fehler), dann `build.py`,
damit `assets/dist/` konsistent bleibt.
