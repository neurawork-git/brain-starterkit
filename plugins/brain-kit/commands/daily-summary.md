---
description: Tagesbericht aus Tageslog, Commits, Compile-Stand und offenen Entscheidungen
---

# Tages-Zusammenfassung

Was heute passiert ist, in 30 Sekunden lesbar. Quellen sind das Tageslog des
Graphen, das Compile-Log, die Commits und die offenen Entscheidungen — alles
Vorhandenes, nichts Nachgehaltenes.

---

## STEP 1: Tageslog lesen

`$BRAIN_ROOT/.daily/YYYY-MM-DD.md` (heute). Ist `BRAIN_ROOT` nicht gesetzt, melde
das und arbeite mit den übrigen Quellen weiter.

Fehlt die Datei, heißt das nicht „nichts passiert", sondern dass noch keine Sitzung
geendet hat. Sag das so.

## STEP 2: Commits einsammeln

Über die Repos, in denen heute gearbeitet wurde:

```bash
git -C <repo> log --since=midnight --author=<eigene Mail> --oneline
```

Ohne bekannte Repo-Liste reicht das aktuelle Repo. Nenne, was du geprüft hast —
eine Zusammenfassung, die verschweigt, wie weit sie geschaut hat, ist wertlos.

## STEP 3: Compile-Stand prüfen

`$BRAIN_ROOT/.daily/compile-log.md`: Wurde heute destilliert, und was kam dabei
heraus? Steht Rückstand an, ist das ein Punkt für die Zusammenfassung —
`/consolidate` löst ihn auf.

## STEP 4: Offene Entscheidungen

`$BRAIN_ROOT/decisions/_queue.md`. Vorschläge, die dort liegen, warten auf einen
Menschen und versanden sonst.

## STEP 5: Ausgeben

```
TAGES-ZUSAMMENFASSUNG — [Datum]

GEARBEITET:
- [aus dem Tageslog: die zwei bis vier Stränge des Tages]

COMMITS:
- [N] Commits in [M] Repos · geprüft: [welche]
- [die wichtigsten Änderungen, eine Zeile je Strang]

WISSEN:
- [N] Nodes neu, [M] aktualisiert (aus dem Compile-Log)
- [oder: Rückstand von [N] Logs — /consolidate ausstehend]

OFFEN:
- [Entscheidungen aus der Queue]
- [Action Items aus dem Tageslog]

[Zwei bis drei Sätze: was erreicht wurde, was hängt.]
```

---

## Regeln

- **Nur tatsächliche Daten** aus den vier Quellen. Nichts ergänzen, was plausibel
  klingt.
- Fehlt eine Quelle, sag welche — kein Ersatz aus dem Gedächtnis.
- Keine Nodes schreiben. Dieser Befehl liest nur.
- Ist wirklich nichts erfasst: „Keine Aktivität heute erfasst." und die Frage, ob
  die Hooks laufen — ein stiller Hook sieht genau so aus wie ein ruhiger Tag.
