# Stufe 3 — Die Befehle

Ab hier arbeitet der Assistent am Gedächtnis mit, statt dass du es von Hand pflegst.
Vier Befehle, die bei uns im Betrieb laufen — keine Nachbauten für dieses Repo.

## Ausführbar hier

[`plugins/brain-kit/`](../plugins/brain-kit/)

```
/plugin marketplace add neurawork-git/brain-starterkit
/plugin install brain-kit@brain-starterkit
```

Sitzung neu starten, sonst tauchen die Befehle nicht auf. Die Befehlsliste wird beim
Start eingelesen.

Ohne Plugin geht es auch: Die vier Dateien aus `plugins/brain-kit/commands/` nach
`~/.claude/commands/` kopieren, ebenfalls Sitzung neu starten.

Alle vier brauchen `BRAIN_ROOT` als absoluten Pfad. Fehlt die Variable, brechen sie
mit einer Meldung ab, statt einen Pfad zu raten.

## Was jeder erledigt

| Befehl | Aufgabe | Wann |
|---|---|---|
| `/primer` | Lädt Index, offene Entscheidungen, Projekt-Kontext und die jüngste Arbeit | Beginn einer Sitzung, in die du Kontext brauchst |
| `/diary` | Sichert den Ertrag der laufenden Sitzung ins Tageslog | Mitten in einer langen Sitzung, oder wenn das Capture nicht lief |
| `/consolidate` | Destilliert unverarbeitete Tageslogs zu typisierten Nodes und zieht den Index nach | Wenn Rohmaterial liegen geblieben ist |
| `/daily-summary` | Tagesbericht aus Tageslog, Commits, Compile-Stand und offenen Entscheidungen | Feierabend |

## Die Arbeitsteilung dahinter

`/diary` schreibt Rohmaterial in ein Tageslog. `/consolidate` macht daraus typisierte
Nodes. Der Refinement-Lauf aus Stufe 5 arbeitet auf den fertigen Nodes.

Wer die drei vermischt, bekommt eines von beidem: Dubletten, weil dasselbe zweimal
destilliert wird, oder einen Lauf, der sein eigenes Ergebnis beim nächsten Mal als
Beleg liest.

Deshalb schreibt `/diary` **keine** Nodes, auch wenn es naheliegt. Rohmaterial und
destilliertes Wissen bleiben getrennt, weil nur so nachvollziehbar bleibt, woher eine
Aussage kommt.

## Zwei Dinge, die sie bewusst nicht tun

**Keine Entscheidung annehmen.** Ein `decision`-Node wird als Vorschlag geschrieben
und in `decisions/_queue.md` gehängt. Annehmen darf nur ein Mensch. Ein Assistent, der
seine eigenen Entscheidungen als Wissen festschreibt, baut sich seine Bestätigung
selbst.

**Nichts löschen.** Widerlegtes bekommt einen datierten Marker mit Gegenbeleg, der
alte Absatz bleibt durchgestrichen stehen. Sonst findet die nächste Sitzung dieselbe
Quelle und läuft denselben Irrweg noch einmal.

## Grenze dieser Stufe

Ein Befehl läuft, wenn du ihn tippst. `/diary` am Ende einer Sitzung vergisst man
genau dann, wenn die Sitzung lang und ertragreich war.

Das ist der Grund für Stufe 4, und der einzige: Dort erledigen Hooks Capture und
Destillieren von selbst, und die Befehle bleiben als Handgriff für den Fall, dass ein
Lauf ausfällt.
