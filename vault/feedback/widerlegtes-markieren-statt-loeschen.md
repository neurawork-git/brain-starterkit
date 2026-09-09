---
name: widerlegtes-markieren-statt-loeschen
description: Eine widerlegte Aussage wird datiert markiert und durchgestrichen, nie entfernt, sonst wird derselbe Irrweg erneut gelaufen.
type: feedback
tags: [graph, konvention, revision]
date: 2026-09-09
---

Wird ein Node durch neue Erkenntnis falsch, ist Löschen die teure Variante: Die
externe Quelle, die zum Irrtum geführt hat, existiert weiter. Ohne Gegenbeleg im
Vault findet die nächste Sitzung dieselbe Quelle und trifft dieselbe Entscheidung.

Stattdessen bleibt der alte Absatz stehen, durchgestrichen, mit einem Marker
darüber:

    ⛔ WIDERLEGT 09.09.2026 — <Gegenbeleg>. Nicht umsetzen.

**Beleg:** Zwei Regeln eines Agenten-Cookbooks wurden 2026 widerlegt; die
markierten Fassungen verhinderten die Wiederholung, gelöschte Passagen taten es nicht.
**Konsequenz:** Kein `git rm` auf einen Node, dessen Aussage sich als falsch
erweist. Nur Marker plus Durchstreichung.

Verwandt: [[jeder-node-braucht-eine-kante]] · [[brain-starterkit]]
