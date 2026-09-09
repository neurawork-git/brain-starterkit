# Stufe 1 — Die Konvention

> **Ausführbar hier:** der Systemprompt weiter unten, plus die Vorlage
> [`vault/templates/node.md`](../vault/templates/node.md) als Format-Referenz.

Für ChatGPT, Claude.ai und jedes andere Web-LLM ohne Dateizugriff. Du hältst das
Wissen selbst und lieferst es mit. Klingt nach Rückschritt, ist die Grundlage:
Alle höheren Stufen automatisieren genau dieses Format.

## Ein Node = eine Datei = eine Aussage

```markdown
---
name: postgres-diskvoll-nur-ueber-dateisystem-diagnostizierbar
description: Freier Platz laut Datenbank-Statistik weicht vom echten Dateisystem ab; nur df im Container zeigt die Wahrheit.
type: claim
tags: [postgres, betrieb, diagnose]
date: 2026-09-09
---

Die Statistiksicht der Datenbank meldete 40 % frei, während Schreibvorgänge
scheiterten. `df -h` im Container zeigte 100 % belegt — die Statistik zählt
gelöschte, aber noch nicht freigegebene Seiten mit.

**Beleg:** Vorfall 07.09.2026, Ticket 214.
**Konsequenz:** Bei „Platte voll" zuerst `df` im Container, nie die DB-Statistik.

Verwandt: [[docker-volume-gibt-platz-nicht-zurueck]] · [[betrieb-checkliste]]
```

Fünf Pflichtfelder, mehr nicht: `name` (kebab-case, gleich dem Dateinamen),
`description` (**ein** Satz — danach wird gesucht), `type`, `tags`, `date`.

## Die sechs Typen

| Typ | Was hinein gehört | Woran du ihn erkennst |
|---|---|---|
| `claim` | eine belegte Einzelaussage | „X verhält sich so, Beleg ist Y" |
| `feedback` | eine Arbeitsregel aus einer Korrektur | „mach künftig X statt Y, weil Z" |
| `reference` | Zugang, Instanz, Zahlenwerk zum Nachschlagen | „wo steht was, welche URL, welche ID" |
| `entity` | Kunde, Anbieter, Werkzeug, Person — die Naben | „alles, was wir über diesen Kunden wissen" |
| `project` | laufender Arbeitsstand | „wo stehen wir, was ist offen" |
| `source` | Rohmaterial: Tageslog, Transkript, Mailverlauf | „hieraus wurde destilliert" |

Im Zweifel `claim`. Ein Node, der zwei Aussagen enthält, sind zwei Nodes.

## Die vier Regeln, die den Unterschied machen

1. **Eine Aussage pro Node.** Sammeldokumente werden nie ganz gefunden, nur
   ganz übersehen.
2. **Jeder Node hat mindestens einen `[[wikilink]]`.** Ein Node ohne Kante ist
   Datenmüll mit Zeitstempel. Ein Link auf etwas noch nicht Geschriebenes ist
   erlaubt — er markiert die nächste Lücke.
3. **Kein Beleg, kein Satz.** Wo eine Zahl oder Behauptung steht, steht die
   Quelle daneben. Unklares gehört unter **Offen:**, nicht in den Fließtext.
4. **Widerlegtes wird nicht gelöscht.** Datierter Marker `⛔ WIDERLEGT
   09.09.2026` mit Gegenbeleg davor, alter Absatz durchgestrichen. Sonst findet
   die nächste Sitzung dieselbe Quelle und läuft denselben Irrweg noch einmal.

## Der Index

Eine Datei `MEMORY.md` an der Wurzel, nur Zeiger, nie Inhalt:

```markdown
## Immer gültig
- Bei „Platte voll" erst `df` im Container → `claims/postgres-diskvoll-....md`

## Kunden
- [[kunde-nord]] · [[anbieter-hosting]]
```

Wächst er über ~20 KB, wird ausgelagert nach `topics/<thema>/INDEX.md` — nicht
gekürzt. Zeiger löschen heißt Wissen verlieren.

## Systemprompt zum Kopieren

In ChatGPT unter Projekt-Anweisungen, bei Claude.ai in die Projekt-Instruktion,
sonst als erste Nachricht:

```text
Du arbeitest mit einem Wissensgraphen aus Markdown-Nodes. Regeln:

1. Bevor du antwortest, prüfe den mitgelieferten Kontext. Steht die Antwort dort,
   antworte daraus und nenne den Node-Namen. Spekuliere nicht darüber hinaus.
2. Fehlt Wissen, sag welcher Node fehlt — erfinde keinen Inhalt und keinen Link.
3. Entsteht im Gespräch eine dauerhafte Erkenntnis (eine belegte Aussage, eine
   Arbeitsregel, ein Zugang), schlage am Ende einen neuen Node vor: vollständige
   Datei im Format unten, inklusive mindestens einem [[wikilink]] auf einen der
   Nodes, die ich dir gegeben habe.
4. Formuliere Node-Inhalte so, dass sie ohne dieses Gespräch verständlich sind.
   Kein "wie besprochen", keine Pronomen ohne Bezug.
5. Widersprechen sich Kontext und neue Information, lösche nichts: schlage einen
   datierten WIDERLEGT-Marker mit Gegenbeleg vor.

Node-Format:
---
name: <kebab-case>
description: <ein Satz, danach wird gesucht>
type: claim | feedback | reference | entity | project | source
tags: [<schlagworte>]
date: <YYYY-MM-DD>
---
<Fließtext mit Beleg. Verwandt: [[link]] · [[link]]>
```

## Der Arbeitsablauf ohne Dateizugriff

1. **Vor der Frage:** die zwei bis fünf Nodes, die zum Thema passen, in den Chat
   kopieren. Wenn du nicht weißt welche, `MEMORY.md` kopieren.
2. **Während:** normal arbeiten.
3. **Am Ende:** „Fass zusammen, was hiervon dauerhaft gilt, als Nodes" — Vorschlag
   prüfen, korrigieren, in deinen Ordner legen.

Schritt 3 ist der einzige, der zählt. Wer ihn zwei Wochen durchhält, hat den
Ordner, der Stufe 2 trägt. Wer ihn auslässt, hat Chatverläufe.

**Grenze dieser Stufe, ehrlich benannt:** Schritt 1 vergisst man. Genau dagegen
existiert Stufe 4 — der Hook macht das Kopieren zur Eigenschaft der Umgebung
statt zur Disziplinfrage.
