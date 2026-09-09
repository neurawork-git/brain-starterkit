---
description: Context Priming — Index, offene Entscheidungen, Projekt-Kontext, jüngste Arbeit laden
---

# Context Priming

Lade den vollständigen Arbeitskontext für diese Session.

---

## STEP 1: Brain laden (kg-Graph)

`$BRAIN_ROOT/MEMORY.md` ist der Lean-Index in den Graphen (typisierte Nodes claim/feedback/
reference/entity/project/source). Orientiere dich über Identität, Präferenzen, laufende Systeme
und die immer geltenden Regeln.

Für gezielten Recall NICHT blind Dateien lesen, sondern: Index → Suche über die
`description`-Zeilen → `[[Wikilinks]]` des Treffers folgen. Ein bis zwei Hops reichen fast immer.

Sind Traversal-Werkzeuge eingerichtet (`brain_search`/`brain_get`/`brain_neighbors` als MCP-Tools,
ein eigenes Recall-Skript, ein Graph-CLI), nutze sie statt der Handsuche. Fehlen sie, ist das kein
Fehler — die Handsuche über `grep` liefert dasselbe, nur langsamer.

## STEP 2: Offene Entscheidungen prüfen (Human-Gate)

Lies `brain/decisions/_queue.md` (falls vorhanden). Die Lern-Engines schreiben `decision`-Nodes nur als
`proposed` + queuen sie — **nur du akzeptierst**. Offene Proposals kurz auflisten, damit sie nicht versanden.

## STEP 3: Projekt-Kontext laden

Lies die lokale `CLAUDE.md` des aktuellen Repos (+ ggf. `docs/`) für projektspezifischen Kontext.

## STEP 4: Letzte Arbeit prüfen

Lies das jüngste Tageslog unter `$BRAIN_ROOT/.daily/` (die letzten ein bis zwei Sitzungsblöcke)
für Kontext über die jüngste Arbeit. Fehlt der Ordner, überspringen und das melden.

## STEP 5: Zusammenfassung

```
KONTEXT GELADEN

AKTUELLES PROJEKT:
- Repo: [Name]  ·  Zweck: [aus CLAUDE.md]

LETZTE ARBEIT:
- [Datum]: [aus dem jüngsten Tageslog]

OFFENE ENTSCHEIDUNGEN: [N aus decisions/_queue.md, oder „keine"]

BRAIN: kg-Graph geladen (Identität, Präferenzen, Hot Rules)
```

---

## Regeln

- Daten aus angebundenen Systemen IMMER live abfragen — nie aus dem Gedächtnis.
- Kompakt halten — Übersicht, nicht Details.
- Graph-First: prüfe den Graphen, bevor du eine Rückfrage stellst (siehe `~/.claude/CLAUDE.md` §8).
- Falls eine Quelle oder der Graph nicht erreichbar ist: melden und mit dem Verfügbaren weitermachen.
