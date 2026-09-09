# Stufe 5 — Dreaming

> **Ausführbar hier:** `/dream` aus [`plugins/brain-kit/`](../plugins/brain-kit/).
> Der Befehl macht der Reihe nach, was bei uns mehrere Agenten parallel tun — die
> Orchestrierung fehlt, das Verfahren nicht. Er schreibt ausschließlich Vorschläge nach
> `$BRAIN_ROOT/.dream/<datum>/` und fasst den Graphen nicht an.

Der Compile aus [Stufe 4](stufe-4-plugin.md) verarbeitet **neues** Rohmaterial zu Nodes. Dreaming
arbeitet auf dem **bestehenden** Graphen: Es liest zurück, was schon da ist, und
sucht, was sich seither verändert hat.

Der Name ist wörtlich gemeint. Nicht neues Erleben, sondern das Nachbereiten des
Erlebten — Zusammenfassen, Verknüpfen, Verwerfen. Menschen tun das nachts, Graphen
brauchen einen geplanten Lauf dafür.

## Was ein Dreaming-Lauf tut

| Aufgabe | Frage, die er beantwortet |
|---|---|
| Widersprüche finden | Behaupten zwei Nodes Gegenteiliges? Welcher ist jünger und besser belegt? |
| Dubletten zusammenführen | Liegt dasselbe Wissen in zwei halben Nodes, von denen die Suche einen findet? |
| Kanten nachziehen | Welche Nodes gehören inhaltlich zusammen und wissen nichts voneinander? |
| Naben verdichten | Ist zu einem Kunden oder Werkzeug genug entstanden, dass er eine eigene Nabe verdient? |
| Ungehobenes Material heben | Liegen Sitzungen, aus denen nie ein Node wurde? |
| Veraltetes markieren | Nennt ein Node eine Datei, ein Flag, eine URL, die es nicht mehr gibt? |

Der teuerste Einzelbefund ist der letzte Punkt. Ein Graph verfällt nicht, indem er
leer wird, sondern indem er unbemerkt recht behält.

## Die zwei Regeln, ohne die es kippt

**1. Der Graph ist während des Laufs schreibgeschützt.** Alle Ergebnisse landen in
einem eigenen Ordner je Lauf, nicht im Vault. Aufnahme nur durch einen Menschen.

Das ist keine Vorsicht, sondern Notwendigkeit: Ein Lauf, der sein eigenes Ergebnis
ins Gedächtnis schreibt, liest es beim nächsten Mal als Beleg. Nach drei Runden
steht dort eine gut verlinkte Überzeugung, die nie jemand geprüft hat.

**2. Alte Quellen destillieren heißt widerlegte Stände wiederbeleben.** Wer alte
Transkripte durchgeht, holt Zwischenstände zurück, die später korrigiert wurden.
Ein Dubletten-Check gegen die Node-Titel fängt das nicht — die alte und die neue
Fassung heißen unterschiedlich. Was hilft: den chronologisch jüngsten Stand zum
Thema **vor** dem Schreiben lesen, und Widersprüche als Befund melden statt als
neuen Node anzulegen.

## Sechs Fragen, bevor du so einen Lauf freigibst

Fehlt eine Antwort, ist der Lauf nicht freigabefähig.

| Element | Frage | Brauchbare Antwort |
|---|---|---|
| Entdeckung | Woher kennt der Lauf seine Arbeit? | Aus geänderten Dateien, Sitzungen, Zeitfenster — **nie** aus einer handgepflegten Aufgabenliste |
| Zustand | Was hält den Stand über Läufe? | Ein Ordner je Lauf plus der Zeitpunkt des letzten. Der nächste setzt dort auf |
| Prüfer | Wer sagt unabhängig „nein"? | Ein gegnerisch gestellter Prüfschritt, der Befunde zu widerlegen versucht |
| Isolation | Wer darf schreiben? | Nur der Mensch, in den Vault. Der Lauf schreibt in seinen eigenen Ordner |
| Kostendeckel | Was stoppt einen leerlaufenden Lauf? | Feste Obergrenze, höchstens eine Wiederholung je Einheit, dann Meldung |
| Haltepunkt | Wo wartet der Lauf zwingend auf einen Menschen? | An der Übernahme-Warteschlange. Unklares wird angehängt, nie entschieden |

## Was du davon brauchst

Für einen Vault unter etwa zweihundert Nodes: nichts davon automatisiert. Setz dir
alle zwei Wochen dreißig Minuten in den Kalender, lass `check.py` laufen und geh
die Befunde durch. Das deckt die ersten vier Zeilen der
Tabelle ab.

Die volle Ausbaustufe ist ein orchestrierter Lauf über Nacht, der jede Rolle einzeln
besetzt: sammeln, bewerten, prüfen, vorschlagen. Sie lohnt sich, wenn mehr Wissen
entsteht, als ein Mensch nebenher überblickt — und sie kostet dann echtes Geld pro
Nacht. Das ist eine Entscheidung über Betriebskosten, keine über Technik.

## Der ehrliche Schlusssatz zu allen fünf Stufen

Automatisierung verbessert, **wie zuverlässig** Wissen erfasst und gefunden wird.
Ob es stimmt, entscheidet weiterhin der Beleg im Node und der Mensch am
Freigabe-Gate. Es gibt keine Stufe 6, die das übernimmt.
