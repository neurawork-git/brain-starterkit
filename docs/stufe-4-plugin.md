# Stufe 4 — Das Plugin

> **Nicht in diesem Repo enthalten.** Die Hooks und der MCP-Server laufen bei uns in
> einem eigenen Plugin, das nicht Teil dieser Veröffentlichung ist. Dieser Text
> beschreibt die Mechanik so, dass man sie nachbauen kann. Den Destillierlauf löst
> [`/consolidate`](stufe-3-befehle.md) von Hand aus — damit ist auch ohne Hooks alles
> erreichbar, nur eben nicht von selbst.

Ab hier ist Erinnern keine Disziplinfrage mehr. Die Umgebung selbst holt vor jedem
Prompt den passenden Ausschnitt des Graphen und legt ihn in den Kontext, und sie
greift am Sitzungsende das Rohmaterial für neue Nodes ab. Beides passiert ohne
Zutun und ohne dass du es formulieren musst.

Der Lauf verarbeitet **neues** Rohmaterial. Das Nachbereiten des **bestehenden**
Graphen ist ein eigener Lauf — siehe [Stufe 5](stufe-5-dreaming.md).

Nur für Claude Code — die Mechanik heißt Hooks, und andere Umgebungen haben sie
nicht in dieser Form.

## Die vier Mechanismen

| Wann | Auslöser | Was passiert |
|---|---|---|
| Vor jedem Prompt | `UserPromptSubmit` | Lexikalische Suche im Graphen, ein Hop entlang der Kanten, kompakter Block als zusätzlicher Kontext |
| Beim Sitzungsende und vor jeder Kompaktierung | `SessionEnd`, `PreCompact` | Transkript-Auszug wird roh in ein Tageslog angehängt. Kein Modellaufruf, unter zehn Sekunden |
| Beim nächsten Sitzungsstart | `SessionStart` | Ist ein Tageslog noch unverarbeitet, startet losgelöst ein Destillierlauf, der daraus typisierte Nodes und den Index schreibt |
| Auf Abruf | MCP-Server | Werkzeuge zum gezielten Traversieren: Index, Suche, Node holen, Nachbarn in bis zu vier Hops |

Der wichtigste der vier ist der zweite Auslöser, `PreCompact`. Er feuert, *bevor*
die Umgebung den vollen Kontext zusammenfasst und verwirft — sonst wäre genau das
Detail weg, das den späteren Node trägt.

## Warum der Compile gebündelt und losgelöst läuft

Destillieren kostet Minuten und Geld. Liefe es beim Sitzungsende, wartest du. Liefe
es bei jedem Node, zahlst du für Zwischenstände. Deshalb: billiges Anhängen am Rand,
ein gebündelter Lauf pro Tag, und der heutige Log ist ausgenommen, weil noch
angehängt wird.

Zwei Fehler aus dem eigenen Betrieb, die du dir sparen kannst:

- **Nicht per Uhrzeit auslösen.** Eine Version feuerte nur, wenn eine Sitzung nach
  18:00 endete, und schaute nur auf heute. Frühere Sitzungen lösten nie aus,
  verpasste Tage kamen nie wieder dran. Der Ordner lief still voll, während jeder
  Hook gesund aussah. Richtig ist aktivitätsgetriggert plus Rückstandsprüfung.
- **Nicht parallel zum Prompt-Hook laufen lassen.** Der Compile schreibt Index und
  Nodes; läuft er, während der Injektions-Hook liest, reißt dessen Zeitschranke.
  Das sieht aus wie ein langsames Skript und ist ein Terminierungsproblem. Ein
  nächtlicher geplanter Lauf löst es, eine höhere Zeitschranke nicht.

## Installation

1. **Vault existiert und ist sauber** (Stufe 2). [`vault/check.py`](../vault/check.py) meldet null Befunde.
2. **Einmalig in `~/.claude/settings.json`** — das kann kein Plugin für dich setzen:

   ```json
   {
     "autoMemoryDirectory": "C:/Pfad/zu/brain",
     "env": { "BRAIN_ROOT": "C:/Pfad/zu/brain" }
   }
   ```

   Absolute Pfade, **kein `~`**. Die Hook-Skripte expandieren die Tilde nicht: Mit
   Tilde meldet die Linkprüfung *jeden* Link als kaputt und die Suche läuft leer —
   beides ohne Fehlermeldung.
3. **Plugin installieren**, Sitzung neu starten.
4. **Positivkontrolle je Hook.** Eine Datei mit einem gültigen Link schreiben: Die
   Prüfung muss schweigen. Einen Prompt zu einem Thema stellen, das im Vault liegt:
   Die Antwort muss den Node nennen.

Schritt 4 ist nicht optional. **Hooks sterben lautlos** — ein Hook ohne Treffer
sieht exakt aus wie ein toter Hook. Nach jedem Pfadwechsel, jedem Umzug und jedem
Plugin-Update wiederholen.

## Die Grenzen, ehrlich

- **Die Injektion ist lexikalisch, nicht semantisch.** Sie findet, was wörtlich
  passt, plus einen Hop. Ein Node, dessen `description` die Wörter nicht enthält,
  die du tippst, wird nicht injiziert. Deshalb ist dieser eine Satz die eigentliche
  Qualitätsarbeit am ganzen Verfahren.
- **Der injizierte Block ist unsichtbar.** Er geht als Zusatzkontext an das Modell
  und erscheint nie im Terminal. Ohne ein Skript, das ihn anzeigt, ist die
  Trefferqualität schlicht unbeobachtbar — und was man nicht misst, verfällt.
- **Das Budget ist fest.** Injiziert werden die besten fünf Treffer. Der Hebel ist
  nicht „mehr injizieren", sondern die Rangfolge: bessere `description`, gesetzte
  `tags`, gezogene Kanten.
- **Automatisch destillierte Nodes sind Vorschläge.** Entscheidungen gehören in
  eine Warteschlange, die ein Mensch abnimmt. Ein Agent, der seine eigenen
  Entscheidungen als Wissen festschreibt, baut sich seine Bestätigung selbst.

## Wann sich Stufe 4 lohnt

Ab etwa hundert Nodes und mehreren Sitzungen pro Tag. Darunter ist der Vault klein
genug, dass die Befehle aus `commands/` ihn zuverlässig überblicken, und der Aufwand
zahlt sich nicht aus.

Das gepackte Plugin gibt es auf Anfrage. Wer es selbst bauen will, braucht drei
Skripte: eines für die Suche mit Kantenexpansion (aufgerufen bei
`UserPromptSubmit`), eines fürs Anhängen des Transkripts (bei `SessionEnd` und
`PreCompact`), eines für den Destillierlauf. Die Suche ist dieselbe, die auch die
Befehle aus `commands/` benutzen — der Unterschied ist allein, wer sie auslöst.
