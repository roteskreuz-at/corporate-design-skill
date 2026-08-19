# Farben — ÖRK Corporate Design

> Quellen: https://design.roteskreuz.at/grundelemente/farben, https://design.roteskreuz.at/grundelemente/farben/analoge-anwendungen, https://design.roteskreuz.at/grundelemente/farben/digitale-anwendungen, https://design.roteskreuz.at/jugendrotkreuz/basiselemente/farben, data/tokens/color.tokens.json · Stand der Erhebung: 2026-08-19
> Verbindlichkeit: cd-verbindlich · Fachlich freigegeben: nein

Die CD-Farben des ÖRK sind Weiß, Schwarz, Rot und Grau. Es gibt ZWEI Rottöne, die strikt zu trennen sind:

- **Logorot** (#FF0000, Pantone 485 C): das helle, strahlende Rot des Wahrzeichens.
- **Dunkelrot** (#B70E0C, Pantone 1805 C): der Arbeitston des CD — aus dem Logorot entwickelt, für Stilelemente, Typografie-Akzente und Flächen.

Hauptfarben sind Dunkelrot, Schwarz und Weiß. Logorot wird sparsam eingesetzt, um die Wirkung des Logos nicht zu schmälern.

## Kanalregel Logorot (Print vs. Digital)

Für Logorot gelten je nach Kanal unterschiedliche Regeln:

| Kanal | Regel |
|---|---|
| **Print/analog** | Logorot AUSSCHLIESSLICH im Wahrzeichen. VERBOTEN als Schriftfarbe, als farbiger Hintergrund und im Layout ("darf ansonsten NICHT MEHR eingesetzt werden"). |
| **Digital** | Zusätzlich als Zusatzfarbe erlaubt: sparsam, max. 10 % Flächenanteil, für Call-to-Actions und Störer. Nicht großflächig, nicht identitätsstiftend. |

Diese Auflösung ist auch in `data/tokens/color.tokens.json` hinterlegt (Feld `kanalregel_logorot`, Status "entschieden-kanalregel", 2026-08-19). Fachliche Bestätigung durch cd@roteskreuz.at steht aus.

## Primärfarben (alle Farbsysteme)

| Farbe | HEX | RGB | CMYK | Pantone | HKS | RAL |
|---|---|---|---|---|---|---|
| Logorot | #FF0000 | 255 \| 0 \| 0 | 0 \| 100 \| 100 \| 0 | 485 C | 13K | 3020 |
| Dunkelrot | #B70E0C | 183 \| 14 \| 12 | 0 \| 100 \| 100 \| 25 | 1805 C | 15K | 3002 |
| Schwarz | #000000 | 0 \| 0 \| 0 | 0 \| 0 \| 0 \| 100 | Black 6 C¹ | 88 | 9017 |
| Grau | #838383 | 131 \| 131 \| 131 | 0 \| 0 \| 0 \| 50 | 430 C | 88; 50 % | 7042 |
| Weiß | #FFFFFF | 255 \| 255 \| 255 | 0 \| 0 \| 0 \| 0 | — | — | 9003 (Signalweiß) |

¹ Das Portal nennt bei den Logofarben "Black 6 C", bei den Typografiefarben "Black C" — unklar, welche Angabe gilt; alle Zahlenwerte sind identisch.

### Grauwert-Falle (häufigster Fehler)

**Pflicht: ÖRK-Grau ist #838383** (RGB 131|131|131 = CMYK 0|0|0|50). Das Office-Standardgrau **#808080 (RGB 128|128|128) ist NICHT das ÖRK-Grau** und darf nicht verwendet werden — es taucht häufig in Bestandsvorlagen auf, weil Office "50 % Grau" als #808080 anbietet.

## Logofarben (analog)

- Rotes Kreuz (Wahrzeichen): Logorot.
- Schriftzug "Österreichisches Rotes Kreuz" und Slogan "Aus Liebe zum Menschen": 100 % Schwarz.
- Landesverbandszusatz (Balken): 50 % Schwarz (= Grau #838383).
- Schwarz-Weiß-Version des Logos: Wahrzeichen in 50 % Schwarz.

## Typografiefarben (analog)

- Schwarz (100 %) und Grautöne mit Deckkraft 99 %–86 % sind der Typografie vorbehalten.
- Zusätzlich als Schriftfarbe erlaubt: alle anderen Grautöne (85 % bis 1 % Schwarz) sowie Weiß. Achtung: helle Grautöne auf hellen Flächen schwer lesbar.
- Dunkelrot in der Typografie AUSSCHLIESSLICH mit 100 % Deckkraft.
- VERBOTEN: alle anderen Farben als Schriftfarbe.

## Layoutfarben (analog)

- Dunkelrot ausschließlich mit 100 % Deckkraft; verwendet in der "Infoleiste" und als rechteckiger, flächiger Hintergrund für Typografie (dort auch mit Foto "multipliziert" möglich).
- Weiß und Grautöne flächig erlaubt: Spektrum von 85 % Schwarz bis 0 % (Weiß), auch Farbverläufe innerhalb dieses Spektrums. Zu helle graue Flächen sind im Druck schwer erkennbar.

## Akzentfarben (analog, genehmigungspflichtig)

Zusätzlich zu den Primärfarben sind in Print- und Onlinepublikationen Akzentfarben möglich — nicht großflächig, sondern für Infografiken und Diagramme. Einzelnen Themengebieten können Akzentfarben als Schmuckfarben zugeordnet werden (Farbleitsystem in Lern-/Lehrmaterialien). **Pflicht: Ein solcher Einsatz bedarf der Genehmigung des ÖRK-Generalsekretariats (cd@roteskreuz.at).**

Die verbindlichen Werte laut CD-Handbuch (Quelle: https://design.roteskreuz.at/fileadmin/user_upload/Print/Grundelemente/Farben/Akzentfarben.pdf, ausgelesen 2026-08-19):

| Akzentfarbe | CMYK | RGB | Hex |
|---|---|---|---|
| Hellblau | 75 \| 0 \| 20 \| 5 | 0 \| 172 \| 193 | #00ACC1 |
| Dunkelblau | 100 \| 35 \| 0 \| 25 | 0 \| 101 \| 160 | #0065A0 |
| Violett | 65 \| 62 \| 5 \| 0 | 111 \| 105 \| 163 | #6F69A3 |
| Lila | 40 \| 65 \| 0 \| 100 * | 166 \| 109 \| 167 | #A66DA7 |
| Orange | 0 \| 50 \| 100 \| 0 | 242 \| 148 \| 0 | #F29400 |
| Gelb | 0 \| 20 \| 100 \| 10 | 235 \| 189 \| 0 | #EBBD00 |
| Hellgrün | 40 \| 0 \| 65 \| 15 | 154 \| 184 \| 106 | #9AB86A |
| Helltürkis | 50 \| 0 \| 30 \| 5 | 134 \| 196 \| 183 | #86C4B7 |
| Dunkeltürkis | 75 \| 0 \| 40 \| 20 | 13 \| 150 \| 142 | #0D968E |
| Dunkelgrün | 75 \| 0 \| 75 \| 20 | 44 \| 145 \| 85 | #2C9155 |

\* Unklar: Der CMYK-Wert von Lila (K=100) steht so im offiziellen PDF, widerspricht aber offensichtlich dem RGB/Hex-Wert (K=100 ergäbe nahezu Schwarz — vermutlich Tippfehler im Handbuch, plausibel wäre K=0). Für Druck vor Verwendung bei cd@roteskreuz.at klären; für Digital gilt der Hex-Wert.

## Digitale Anwendungen

### Hauptfarben (digital)

Für große Farbflächen und Text: Dunkelrot #B70E0C, Schwarz #000000, Weiß #FFFFFF (Werte wie oben).

### Zusatzfarben (digital, je max. 10 % Flächenanteil)

Ergänzende Funktion, nicht identitätsstiftend, nicht großflächig — für Call-to-Actions und Störer. Verhältnis zu den restlichen verwendeten Farben/Bildern: je max. 10 %; der überwiegende Rest ist z. B. Weiß, Dunkelrot oder Bildinhalt.

| Farbe | HEX | RGB | CMYK | RAL |
|---|---|---|---|---|
| Grau | #838383 | 131 \| 131 \| 131 | 0 \| 0 \| 0 \| 50 | 7042 |
| Dunkelblau | #002D55 | 0 \| 45 \| 85 | 100 \| 45 \| 0 \| 65 | 5026 |
| Logorot | #FF0000 | 255 \| 0 \| 0 | 0 \| 100 \| 100 \| 0 | 3020 |

(Pantone/HKS für Dunkelblau nicht dokumentiert.)

### Farbabstufungen (digital)

Für Icons und Infografiken; unterstützen Logo und Hauptfarben. Pantone/HKS nicht dokumentiert.

**Rotabstufungen:**

| HEX | RGB | CMYK | RAL |
|---|---|---|---|
| #F4DCDB | 244 \| 220 \| 219 | 5 \| 20 \| 10 \| 0 | 9001 |
| #E39E9E | 227 \| 158 \| 158 | 10 \| 45 \| 30 \| 0 | 3015 |
| #D46E6E | 212 \| 110 \| 110 | 15 \| 65 \| 45 \| 5 | 4010 |
| #C43D3D | 196 \| 61 \| 61 | 15 \| 85 \| 75 \| 5 | 3020 |
| #8A0A0A | 138 \| 10 \| 10 | 30 \| 100 \| 100 \| 35 | 3002 |
| #5C0805 | 92 \| 8 \| 5 | 35 \| 100 \| 90 \| 60 | 3005 |

**Blauabstufungen:**

| HEX | RGB | CMYK | RAL |
|---|---|---|---|
| #0065A0 | 0 \| 101 \| 160 | 90 \| 55 \| 10 \| 0 | 5005 |
| #B4D8EB | 180 \| 216 \| 235 | 35 \| 5 \| 5 \| 0 | 5024 |

**Grauabstufungen:**

| HEX | RGB | CMYK | RAL |
|---|---|---|---|
| #C6C6C6 | 198 \| 198 \| 198 | 25 \| 20 \| 20 \| 0 | 7047 |
| #F6F6F6 | 246 \| 246 \| 246 | 5 \| 5 \| 5 \| 0 | 7035 |

### Erweiterte Farbwelt ("Farbenparkplatz", nur Empfehlung)

Kann-Bestimmungen für Grafik-Design-Profis; bei Anwendungsfragen Marketingabteilung des Landesverbands kontaktieren.

| HEX | RGB | CMYK | RAL |
|---|---|---|---|
| #00ACC1 | 0 \| 172 \| 193 | 75 \| 15 \| 25 \| 0 | 5018 |
| #0065A0 | 0 \| 101 \| 160 | 90 \| 55 \| 10 \| 0 | 5005 |
| #6F69A3 | 111 \| 105 \| 163 | 65 \| 60 \| 10 \| 0 | 4005 |
| #A66DA7 | 166 \| 109 \| 167 | 40 \| 65 \| 5 \| 0 | 4008 |
| #E3006A | 227 \| 0 \| 106 | 0 \| 100 \| 25 \| 0 | 4010 |
| #F29400 | 242 \| 148 \| 0 | 0 \| 50 \| 100 \| 0 | 2007 |
| #EBBD00 | 235 \| 189 \| 0 | 10 \| 25 \| 95 \| 0 | 1021 |
| #9AB86A | 154 \| 184 \| 106 | 50 \| 10 \| 70 \| 0 | 6018 |
| #86C4B7 | 134 \| 196 \| 183 | 50 \| 5 \| 35 \| 0 | 6027 |
| #0D968E | 13 \| 150 \| 142 | 80 \| 20 \| 50 \| 0 | 5018 |
| #2C8155 | 44 \| 129 \| 85 | 80 \| 25 \| 80 \| 10 | 6024 |

### Sonderfarben (Get-Social)

Farben aus dem CD des Jugendrotkreuzes und der Kampagnenwelt "Get-Social"; insbesondere für junge Zielgruppen und bestimmte Projekte/Programme (z. B. Stammzellspende). Werte siehe Abschnitt Jugendrotkreuz.

## Jugendrotkreuz (JRK)

- **CD-Farben: identisch mit dem ÖRK** — Weiß, Schwarz, Rot, Grau; Logorot nur im Logo, nicht in Typografie oder Schmuckfarben.
- **Akzentfarben:** wie ÖRK (siehe Akzentfarben analog).
- **Zusätzlich: Get-Social-Farbwelt** für die zielgruppengerechte Ansprache von Kindern, Jugendlichen und Betreuungspersonen. Hauptfarbe ist Dunkelviolett (Farbe 1); die übrigen sind die im Get-Social-Herz verwendeten Farben.

| Farbe | HEX | RGB | CMYK | Pantone |
|---|---|---|---|---|
| Farbe 1 (Dunkelviolett, Hauptfarbe) | #403A60 | 64 \| 58 \| 96 | 86 \| 83 \| 9 \| 45 | 5265 C |
| Farbe 2 | #7C7FAB | 124 \| 127 \| 171² | 55 \| 48 \| 6 \| 0 | 7675 C |
| Farbe 3 | #99D6EA | 153 \| 214 \| 234 | 34 \| 0 \| 5 \| 0 | 2975 C |
| Farbe 4 | #A0DAB3 | 160 \| 218 \| 179 | 32 \| 0 \| 30 \| 0 | 344 C |
| Farbe 5 | #F8A3BC | 248 \| 163 \| 188 | 0 \| 39 \| 10 \| 0 | 189 C |
| Farbe 6 | #FF808B | 255 \| 128 \| 139 | 0 \| 54 \| 38 \| 0 | 177 C |
| Farbe 7 | #F2E5AA | 242 \| 229 \| 170 | 0 \| 13 \| 48 \| 0 | 2001 C |
| Get-Social-Typofarbe | #3F3A66 | 63 \| 58 \| 102 | 82 \| 82 \| 29 \| 20 | nicht dokumentiert |

² Unklar: Die JRK-Seite nennt RGB 124|127|171 (konsistent mit #7C7FAB), die Seite "Digitale Anwendungen" für dieselbe Farbe RGB 125|128|171. Der Hex-Wert #7C7FAB entspricht 124|127|171.

Hinweis: Die CMYK-Werte der Get-Social-Farben unterscheiden sich zwischen der Seite "Digitale Anwendungen" (Sonderfarben, z. B. Farbe 1: 85|80|35|25) und der JRK-Seite (Farbe 1: 86|83|9|45). Für JRK-Anwendungen gelten die Werte der JRK-Seite (oben); die Abweichung ist im Portal nicht erklärt.

## Warnliste: Diese Werte NICHT verwenden

Systematischer Befund aus color.tokens.json: Das Theme der PowerPoint-Vorlage (POTX 2026) führt die offizielle Rotreihe durchgängig leicht verfälscht. Die Vorlage ist gegen diese Referenz zu korrigieren — nicht umgekehrt.

| Falscher Wert (Vorlage) | Richtiger Wert (offiziell) | Fundstelle des Fehlers |
|---|---|---|
| #B70F0B | **#B70E0C** | theme1.xml → a:dk2 (ebenso a:hlink/a:folHlink) |
| #B70E0B | **#B70E0C** | Folienlayout 10 "Aussage 1", hart eingetragener Hintergrund |
| #D46D6E | **#D46E6E** | theme1.xml, Rotabstufung |
| #C33C3C | **#C43D3D** | theme1.xml, Rotabstufung |
| #89090A | **#8A0A0A** | theme1.xml, Rotabstufung |
| #5B0804 | **#5C0805** | theme1.xml, Rotabstufung |
| #808080 | **#838383** | Office-Standardgrau in Bestandsvorlagen (häufigster Fehler) |

Ebenfalls VERBOTEN (aus color.tokens.json, Negativliste):

- **Gold #D4AF37**: kommt im ÖRK-CD nicht vor.
- **Weißes Kreuz auf rotem Grund** (Logorot als Emblem-Hintergrund): das ist das Schweizer Wappen (RKG § 8 Abs. 2) — rechtliche Ebene, kein Gestaltungsspielraum. Ebenso untersagt: inverse Schrift/Kontur, Logo auf Bild ohne weißen Hintergrund.

## Kontakt

Freigaben und Fragen: ÖRK-Generalsekretariat, cd@roteskreuz.at; Anwendungsfragen: Marketingabteilung des jeweiligen Landesverbands.
