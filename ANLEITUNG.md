# Anleitung: das ÖRK-CD-Regelwerk in KI-Werkzeuge einbinden

Dieses Repository enthält das Corporate Design des Österreichischen Roten Kreuzes in maschinenlesbarer Form. Es ist als Claude-Skill gebaut, die Inhalte funktionieren aber in jedem KI-Werkzeug, das Kontextdateien annimmt. Diese Anleitung beschreibt beide Wege.

Stand: August 2026. Menüpfade und Limits der einzelnen Anbieter ändern sich laufend; die Dateistruktur dieses Repos ist die stabile Grundlage.

## Vorab: Regeln, die überall gelten

1. Die [KI-Richtlinie des ÖRK](https://design.roteskreuz.at/fileadmin/user_upload/Digitales_CD/Grundlagen/Rechtliches/OeRK_KI_Richtlinien.pdf) ist eine Weisung. Mitarbeitende dürfen nur KI-Anwendungen nutzen, die auf der gelben oder grünen Liste des KI-Boards stehen (https://kurse.roteskreuz.at/static/kiboard.html), und müssen die Schulung „Künstliche Intelligenz – Basiswissen" absolviert haben. Vor dem Einrichten eines der folgenden Werkzeuge also zuerst dort nachsehen.
2. Das rote Kreuz darf von keiner KI erzeugt, nachgezeichnet oder verändert werden. Es gelten das Rotkreuzgesetz und die Genfer Abkommen; Details in `references/emblemrecht.md`. Logos kommen ausschließlich aus `assets/logos/` oder vom Portal.
3. KI-generierte Inhalte, die den Anschein von Realität erwecken oder ungeprüft veröffentlicht werden, sind als solche zu kennzeichnen.
4. Kein Inhalt dieses Repos ist fachlich freigegeben (`human_verified: false`). Alles, was damit entsteht, ist ein Entwurf; die Freigabe liegt bei cd@roteskreuz.at bzw. beim Landesverband.

## Welche Dateien wofür

| Datei/Ordner | Inhalt | Wichtig für |
|---|---|---|
| `SKILL.md` | Kernwerte, Leitplanken, Arbeitsablauf | jede Einbindung — das ist die Basisinstruktion |
| `references/farben.md`, `typografie.md`, `logo.md`, `emblemrecht.md` | die vier Grundreferenzen | jede Gestaltungsaufgabe |
| `references/markenkommunikation.md` | Tonalität, verbindliche Schreibweisen | jede Texterstellung |
| übrige `references/*.md` | Digital, Print, Branding, Audio/Video, JRK, Prüfen | je nach Aufgabe |
| `data/tokens/*.json` | W3C-Design-Tokens (Quelle der Wahrheit) | Automatisierung, Design-Werkzeuge |
| `assets/dist/` | Office-Theme, Adobe-ASE, CSS | direkte Nutzung ohne KI |
| `assets/logos/` | Original-Logodateien | jedes Deliverable mit Logo |

Wenn ein Werkzeug die Zahl der Dateien begrenzt, diese Reihenfolge einhalten: `SKILL.md`, dann die vier Grundreferenzen, dann `markenkommunikation.md`, dann aufgabenspezifische Referenzen.

## Claude Code (Terminal, Desktop-App, IDE-Erweiterungen)

Der native Weg — das Repo ist ein fertiger [Agent Skill](https://code.claude.com/docs/en/skills).

Persönlich (gilt in allen Projekten):

```bash
git clone https://github.com/roteskreuz-at/corporate-design-skill ~/.claude/skills/oerk-cd
```

Pro Projekt (gilt für alle, die im Projekt arbeiten): in das Projektverzeichnis nach `.claude/skills/oerk-cd` klonen und die Dateien einchecken oder als Submodule führen.

Danach ist nichts weiter zu tun. Claude erkennt Anfragen mit Rotkreuz-Bezug selbst und lädt die passenden Referenzen; testen lässt sich das mit einer Frage wie „Welches Rot nehme ich für Überschriften in einem ÖRK-Flyer?". Aktualisieren per `git pull`.

## Claude.ai und Claude-Desktop (Web/App)

Zwei Wege:

Als Skill (empfohlen, sofern der Tarif Skills unterstützt): Repo als ZIP packen und in den Einstellungen unter Fähigkeiten/Skills hochladen.

```bash
git clone https://github.com/roteskreuz-at/corporate-design-skill
cd corporate-design-skill && zip -r ../oerk-cd.zip . -x ".git/*"
```

Als Projektwissen: ein Claude-Projekt anlegen (z. B. „ÖRK Corporate Design"), `SKILL.md` und die benötigten `references/*.md` als Projektdateien hochladen und den Inhalt von `SKILL.md` (Abschnitte „Harte Leitplanken" und „Kernwerte") in die Projektanweisungen übernehmen. Alle Chats in diesem Projekt arbeiten dann mit dem Regelwerk.

## Claude API / Agent SDK

Für eigene Anwendungen (z. B. einen internen Assistenten): Das Agent SDK lädt Skills aus einem Skills-Verzeichnis — das geklonte Repo dort ablegen, fertig. Bei direkter Nutzung der Messages API den Inhalt von `SKILL.md` in den System-Prompt übernehmen und die jeweils benötigten Referenzdateien als Kontext mitgeben. Für strukturierte Abfragen (etwa einen Farb-Lookup) direkt `data/tokens/color.tokens.json` verwenden statt der Markdown-Fassung.

## ChatGPT (Projekte oder Custom GPT)

ChatGPT kennt kein Skill-Format, nimmt aber Wissensdateien an:

1. Projekt oder Custom GPT anlegen (z. B. „ÖRK Corporate Design").
2. Als Anweisungen den Inhalt von `SKILL.md` einfügen; die Pfadverweise auf `references/…` durch den Hinweis ersetzen, dass diese Dateien im Wissen liegen.
3. Die `references/*.md` als Wissensdateien hochladen (bei Datei-Limits: Reihenfolge von oben; notfalls mehrere Referenzen zu einer Datei zusammenfügen).

Zu beachten: ChatGPT lädt Wissensdateien per Suche, nicht vollständig — bei Wertfragen (Hex, CMYK) das Ergebnis gegen `references/farben.md` gegenprüfen, bevor etwas in Produktion geht.

## OpenAI Codex (CLI)

Repo klonen und in der `AGENTS.md` des Arbeitsprojekts verankern:

```markdown
## ÖRK Corporate Design
Bei allen Aufgaben mit Rotkreuz-Bezug gilt das Regelwerk unter
~/corporate-design-skill/ — zuerst SKILL.md lesen, dann die dort
verlinkten references/. Das rote Kreuz niemals generieren.
```

## Gemini CLI / Antigravity

Gleiches Prinzip über die Kontextdatei des Werkzeugs (`GEMINI.md` bzw. Projektkontext): Repo klonen, in der Kontextdatei auf `SKILL.md` verweisen und die Emblem-Regel wörtlich hineinschreiben. Bei Werkzeugen ohne Dateizugriff die vier Grundreferenzen direkt in die Kontextdatei kopieren.

## GitHub Copilot

In Repositories, in denen ÖRK-Material entsteht (etwa Web-Projekte): das Regelwerk als Ordner oder Submodule ins Repo nehmen und in `.github/copilot-instructions.md` darauf verweisen — mit den Kernwerten (Dunkelrot `#B70E0C`, Grau `#838383`, Schrift Dunant mit Arial/Helvetica-Fallback) direkt in der Instructions-Datei, damit sie ohne Dateizugriff wirken. Für CSS-Projekte zusätzlich `assets/dist/oerk-farben.css` einbinden, dann stimmen die Werte unabhängig von der KI.

## Cursor, Windsurf und ähnliche KI-Editoren

Rules-Datei des Editors (`.cursor/rules/` bzw. `.windsurfrules`) mit zwei Teilen befüllen: die Kernwerte-Tabelle und die harten Leitplanken aus `SKILL.md` wörtlich, dazu der Verweis auf das geklonte Repo für Details. KI-Editoren folgen Rules zuverlässiger als Dateiverweisen — die kritischen Werte gehören deshalb direkt in die Rule.

## Microsoft 365 Copilot

Über einen deklarativen Agenten (Copilot Studio): Agent anlegen, die `references/*.md` als Wissensquelle hochladen (oder eine SharePoint-Bibliothek mit den Dateien anbinden) und die Leitplanken aus `SKILL.md` als Anweisungen setzen. Alternativ ohne Agent: das korrekte Office-Theme aus `assets/dist/theme1.xml` in die Word-/PowerPoint-Vorlagen einbetten — dann stimmen Farben und Schriften unabhängig davon, was Copilot vorschlägt.

## Ohne KI: die Artefakte direkt nutzen

Vieles aus diesem Repo braucht gar keine KI:

| Artefakt | Verwendung |
|---|---|
| `assets/dist/theme1.xml` | in DOTX/POTX den Pfad `*/theme/theme1.xml` ersetzen — Office zeigt dann die richtigen ÖRK-Farben und -Schriften an |
| `assets/dist/OERK-Farben.ase` | InDesign/Illustrator/Photoshop: Fenster → Farbfelder → Farbfelder laden |
| `assets/dist/oerk-farben.css` | direkt in Web-Projekte einbinden |
| `data/tokens/*.json` | W3C-Design-Tokens-Format — Style Dictionary, Tokens Studio (Figma), Penpot und Supernova lesen das nativ |

## Für Betreiber: das Muster auf design.roteskreuz.at übernehmen

Die nachhaltigste Einbindung wäre keine pro Werkzeug, sondern eine an der Quelle: Das Portal liefert eine `llms.txt` und je Seite eine Markdown-Fassung aus, und die `robots.txt` gibt einen Pfad (z. B. `/cd/`) für maschinelles Abrufen frei — dann beantworten künftig alle KI-Systeme ÖRK-Fragen aus der Originalquelle statt aus Rekonstruktionen. Die Internationale Föderation macht das unter brand.ifrc.org bereits vor. Eine Vorlage für die `llms.txt` liegt in diesem Repo unter `data/llms.txt`; die Umsetzung gehört zum Web-Team (Ansprechpartner: cd@roteskreuz.at).

## Aktuell halten

Das Regelwerk ändert sich, wenn das Portal sich ändert. Bei geklonten Installationen genügt `git pull`; hochgeladene Kopien (Claude.ai-ZIP, ChatGPT-Wissen, Copilot-Agent) müssen nach jedem Update neu hochgeladen werden. Wer eine Abweichung zwischen Repo und Portal findet: Issue in diesem Repository eröffnen oder direkt an den Repo-Verantwortlichen.
