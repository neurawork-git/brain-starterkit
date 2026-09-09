---
name: jeder-node-braucht-eine-kante
description: Ein Node ohne ein- und ausgehende Wikilinks wird von Suche und Injektion nie erreicht und ist damit wertlos.
type: feedback
tags: [graph, konvention, qualitaet]
date: 2026-09-09
---

Beim Aufräumen eines gewachsenen Vaults waren 101 von rund 900 Nodes in der
Obsidian-Graphenansicht isoliert: inhaltlich gut, aber ohne Kante. Keiner davon
war je in einer Antwort aufgetaucht.

Die Zählweise ist die Falle: Wer nur eingehende Kanten prüft, meldet doppelt so
viele Waisen wie es gibt. Isoliert ist ein Node erst, wenn **weder** eine Kante
hinein **noch** eine hinaus führt. Ein Verweis aus der Index-Datei zählt nicht als
Anbindung — der Index verlinkt fast alles und würde jede Waise übertünchen.

**Beleg:** Aufräumlauf 03.09.2026, Zählung vor/nach Korrektur der Metrik.
**Konsequenz:** Beim Schreiben eines Nodes gleich mindestens eine Kante
setzen, auch auf etwas noch Ungeschriebenes. `check.py` meldet Waisen.

Verwandt: [[widerlegtes-markieren-statt-loeschen]] · [[brain-starterkit]]
