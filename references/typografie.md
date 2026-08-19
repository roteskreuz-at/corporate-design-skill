# Typografie
> Quellen: https://design.roteskreuz.at/grundelemente/typografie, https://design.roteskreuz.at/digital/social-media/typografie, data/tokens/typography.tokens.json · Stand der Erhebung: 2026-08-19
> Verbindlichkeit: cd-verbindlich · Fachlich freigegeben: nein

## Hausschrift: Dunant

Pflicht: Die Hausschrift Dunant ist in allen Kommunikationsmitteln des ÖRK einzusetzen (Ausnahmen siehe unten).

- Fünf Schriftschnitte: **Light, Regular, Medium, Bold, Signs**.
- "Signs" ist laut Token-Datei ein Symbol-/Zeichensatz, kein Textschnitt — nicht für Fließtext verwenden (Einordnung aus JSON, im Portaltext nicht näher beschrieben).
- Plattformübergreifende OTF (OpenType Font) für Windows und Mac OS.

Gewichts-Zuordnung (aus typography.tokens.json, abgeleitet):

| Schnitt | fontWeight |
|---|---|
| Light | 300 |
| Regular | 400 |
| Medium | 500 |
| Bold | 700 |
| Signs | 400 (Symbolsatz) |

### Download (Portal)
- Dunant (OTF, ZIP): https://design.roteskreuz.at/fileadmin/user_upload/Print/Grundelemente/Schrift/Dunant.zip
- Dunant Web-Fonts (ZIP): https://design.roteskreuz.at/fileadmin/user_upload/Print/Grundelemente/Schrift/Web-Fonts.zip

### Lizenz
Das Portal stellt die Dunant selbst als OTF-ZIP und Web-Fonts-ZIP bereit; ein expliziter Lizenztext ist nicht dokumentiert. Laut Token-Datei bleibt offen, ob die Lizenz die Einbettung in automatisiert erzeugte Dokumente und die Weitergabe an Dritte abdeckt — im Zweifel cd@roteskreuz.at bzw. die Marketingabteilung des Landesverbands fragen.

## Ersatzschrift: Arial / Helvetica

Die Ersatzschriften sind vorinstallierte Systemschriften und damit frei nutzbar.

- **Arial** (Windows) bzw. **Helvetica** (Mac) — ausschließlich, wenn die Dunant aus technischen Gründen nicht verwendbar ist (Schrift nicht installierbar), NICHT als gestalterische Alternative.
- Verwendete Schnitte analog zur Dunant: **Arial Bold** und **Arial Regular**.
- Ersatz für Dunant Light ist **Arial Regular**.
- Font-Stacks (Token): Hausschrift `Dunant, Arial, Helvetica, sans-serif`; Ersatz `Arial, Helvetica, sans-serif`.

VERBOTEN: Verdana als Ersatzschrift. Diese Angabe stammte aus einer Fehlableitung aus einer Word-Vorlage (dokumentierte Korrektur vom 2026-08-04 in typography.tokens.json); der offizielle Styleguide nennt nur Arial bzw. Helvetica.

### Ausnahmen von der Hausschrift-Pflicht
1. **E-Mail / Online-Briefverkehr, offizielle ÖRK-Websites, Social-Media-Kanäle**, die die Dunant nicht unterstützen: Arial bzw. Helvetica (Mac) zulässig.
2. **Periodisch erscheinende ÖRK-Magazine/Zeitschriften**: wegen individueller Layouts und deren Wiedererkennbarkeit dürfen andere Schriften verwendet werden.

## Schmuckschrift

Es ist bewusst KEINE Schmuckschrift für die digitale Anwendung definiert (würde das Markenbild schwächen). In Einzelfällen (z. B. Team-Österreich-Tafel-Jubiläumslogo) nur nach Rücksprache mit der Marketingabteilung des jeweiligen Landesverbands gestattet.

## Größen und Stile (aus typography.tokens.json)

Achtung Geltungsbereich: Die Punktgrößen stammen aus der Word-Vorlage Skriptum.dotx und gelten für das Format Skriptum/A4. Sie sind KEINE allgemeine Typoskala für alle Medien; für Digital fehlt eine eigene Skala (so ausdrücklich in der Token-Datei vermerkt).

| Token | Größe |
|---|---|
| footer | 7 pt |
| quellenhinweis | 8 pt |
| body | 10 pt |
| ueberschrift-4 | 12 pt |
| ueberschrift-3 | 12 pt |
| ueberschrift-2 | 14 pt |
| ueberschrift-1 | 16 pt |
| verzeichnis | 20 pt |
| untertitel | 24 pt |
| titel | 36 pt |

Zusammengesetzte Stile (Schrift jeweils Hausschrift-Stack):

| Stil | Schnitt | Größe | Zeilenabstand |
|---|---|---|---|
| deckblatt-titel | Regular (400) | 36 pt | 1.15 |
| deckblatt-untertitel | Regular (400) | 24 pt | 1.2 |
| ueberschrift-1 | Medium (500) | 16 pt | 1.25 |
| ueberschrift-2 | Medium (500) | 14 pt | 1.3 |
| body | Regular (400) | 10 pt | 1.4 |
| footer | Light (300) | 7 pt | 1.2 |

## Typografie auf Social Media

Quelle: https://design.roteskreuz.at/digital/social-media/typografie

### Schriftgrößen & Zeilenabstand
- **Headline**: Mindestgröße **45 pt**, nicht unterschreiten. Optimaler Zeilenabstand = **100 % der Versalhöhe** (Beispiel: Schriftgröße 105 pt → Zeilenabstand 105 pt).
- **Subline und Informationstext**: Mindestgröße **30 pt**. Zeilenabstand: automatische Einstellung.
- **Textausrichtung**: linksbündig.
- **Laufweite**: standardmäßig **10 pt**; für CTA-Text und Text im Orts-Pin **0 pt**.

### Text & Farbe
- Headlinetext vorwiegend in Dunkelrot auf weißem Hintergrund; alternativ Weiß auf dunkelrotem Hintergrund.
- Empfehlung: Subline- und Informationstext auf weißem Hintergrund in Schwarz.
- Fragezeichen und Ausrufezeichen dürfen verwendet werden.

### Textmenge & Hierarchie (Social-Media-Grafiken und Online-Banner)
- Grundregel: "So viel Text wie nötig, so wenig wie möglich."
- Asset muss schnell erfassbar sein; dichte Textblöcke vermeiden; Hauptbotschaft präzise auf den Punkt; keine unwichtigen/wiederholenden Informationen.
- Zu viel Text wird leicht ignoriert und verschlechtert die Performance der Assets.
- Die konkrete Hierarchie-Tabelle der Textelemente liegt nur als Abbildung vor (Detail nur als Abbildung im Portal, Text nicht verfügbar: https://design.roteskreuz.at/digital/social-media/typografie).

## Praxis: Dokumenterzeugung

Pflicht-Ablauf vor jeder Dokument-/Grafikerzeugung:
1. Prüfen, ob die Dunant auf dem System installiert ist (bzw. die Web-Fonts eingebunden werden können).
2. Falls nicht: Arial (Windows) bzw. Helvetica (Mac) verwenden — Zuordnung: Dunant Bold → Arial Bold, Dunant Regular → Arial Regular, Dunant Light → Arial Regular.
3. Das Deliverable ausdrücklich kennzeichnen, dass die Ersatzschrift verwendet wurde (z. B. Hinweis an den Auftraggeber), damit vor finaler Produktion auf Dunant umgestellt werden kann.

---

**Fußnote JRK (bekannter offener Punkt):** 47 der 49 JRK-InDesign-Vorlagen referenzieren einen Schnitt "Dunant School", der weder im Styleguide dokumentiert noch downloadbar ist. Daraus ist keine Regel ableitbar; Status unklar. Die JRK-Portalnavigation verweist für "Schrift" auf die allgemeine Typografie-Seite (/grundelemente/typografie).
