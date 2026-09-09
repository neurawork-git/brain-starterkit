---
description: Refinement-Lauf über den bestehenden Graphen — Widersprüche, Dubletten, fehlende Kanten, Veraltetes; Vorschläge zur Freigabe, keine Änderung
---

# Dreaming — den Graphen nachbereiten

Nicht neues Wissen aufnehmen, sondern das vorhandene nachbereiten: zusammenfassen,
verknüpfen, verwerfen. Menschen tun das nachts, ein Graph braucht einen Lauf dafür.

`/consolidate` verarbeitet **neues** Rohmaterial. Dieser Befehl arbeitet auf den
**bestehenden** Nodes und rührt sie nicht an.

---

## Die eiserne Regel

**Der Graph ist während des ganzen Laufs schreibgeschützt.** Kein Node wird geändert,
keiner gelöscht, keiner angelegt. Alles landet unter
`$BRAIN_ROOT/.dream/YYYY-MM-DD/`. Übernehmen darf nur der Mensch.

Das ist keine Vorsicht, sondern Notwendigkeit: Ein Lauf, der sein Ergebnis in den
Graphen schreibt, liest es beim nächsten Mal als Beleg. Nach drei Runden steht dort
eine gut verlinkte Überzeugung, die nie jemand geprüft hat.

Ist `BRAIN_ROOT` nicht gesetzt, melde das und brich ab.

## STEP 1: Umfang festlegen und ansagen

Zähle die Nodes und nenne die Zahl, bevor du anfängst. Ab etwa 300 Nodes arbeite in
einem Ausschnitt — ein Thema, ein Ordner, oder die seit dem letzten Lauf geänderten
Dateien — und sag, welchen Ausschnitt du nimmst.

**Obergrenze: höchstens zwölf Befunde pro Lauf.** Lieber zwölf geprüfte als vierzig
behauptete. Was nicht mehr hineinpasst, wird als „weitere Kandidaten" nur gezählt.

## STEP 2: Kandidaten sammeln

Sechs Fragen an den Bestand:

| Aufgabe | Woran du sie erkennst |
|---|---|
| Widersprüche | Zwei Nodes behaupten Gegenteiliges. Welcher ist jünger und besser belegt? |
| Dubletten | Dasselbe Wissen in zwei halben Nodes, von denen die Suche einen findet |
| Fehlende Kanten | Zwei Nodes zum selben Gegenstand ohne `[[wikilink]]` zueinander |
| Fehlende Naben | Ein Gegenstand taucht in vielen Nodes auf, hat aber keinen `entity`-Node |
| Veraltetes | Ein Node nennt eine Datei, ein Flag, eine URL — existiert das noch? |
| Schwache Auffindbarkeit | `description` und `tags` enthalten nicht die Wörter, die jemand tippen würde |

Der teuerste ist „Veraltetes": Ein Graph verfällt nicht, indem er leer wird, sondern
indem er unbemerkt recht behält. Prüfe genannte Pfade und Flags tatsächlich nach,
statt sie für plausibel zu halten.

## STEP 3: Je Kandidat schärfen und belegen

Für jeden Befund:

1. Behauptung in einem Satz.
2. Die Belegstelle **öffnen** und prüfen, ob sie die Behauptung wirklich trägt, nicht
   nur am Rande berührt.
3. Vorschlag konkret formulieren: welcher Node, welche Zeile, was genau ändern.

Trägt der Beleg nicht, ist das ein Ergebnis — der Kandidat fällt raus.

## STEP 4: Gegen dich selbst prüfen

Geh jeden geschärften Befund noch einmal durch, jetzt als Skeptiker, der ihn
**widerlegen** will. Drei Fragen:

- **Trägt die Evidenz zwingend?** Bei Zweifel oder Zirkelschluss: schwach.
- **Steht das schon im Graphen?** Suche danach. Falls ja, nenne die Datei.
- **Ist das dauerhaft und verallgemeinerbar** oder ein Einzelfall?

Dann ein Verdikt je Befund:

| Verdikt | Bedeutung |
|---|---|
| `VORLEGEN` | stark belegt, neu, verallgemeinerbar |
| `UNKLAR` | teilweise wertvoll, Evidenz oder Neuheit unsicher |
| `VERWERFEN` | schwache Evidenz, Dublette, Rauschen |

**Bei Unsicherheit ist `UNKLAR` oder `VERWERFEN` richtig, nie `VORLEGEN`.** Ein Lauf,
der nichts vorlegt, ist ein gültiges Ergebnis.

## STEP 5: Ergebnis ablegen

Nach `$BRAIN_ROOT/.dream/YYYY-MM-DD/`:

- `vorschlaege.md` — je Befund: Verdikt, Behauptung, betroffene Nodes, Belegstelle,
  vorgeschlagene Änderung im Wortlaut. Nach Verdikt sortiert, `VORLEGEN` zuerst.
- `verworfen.md` — die `VERWERFEN`-Fälle mit Grund. Kurz. Sie verhindern, dass der
  nächste Lauf dieselbe Spur noch einmal verfolgt.

Nichts davon geht in den Graphen.

## STEP 6: Berichten

```
DREAMING — [Datum]

Betrachtet:  [N] Nodes ([Ausschnitt, falls nicht alle])
Kandidaten:  [N] gefunden, [M] nach Belegprüfung übrig
Verdikt:     [N] VORLEGEN · [M] UNKLAR · [K] VERWERFEN
Nicht geprüft: [N] weitere Kandidaten (Obergrenze erreicht)

VORLEGEN:
- [Behauptung] → [Node] ([Belegstelle])
```

Dann eine Frage an den Menschen, welche Vorschläge übernommen werden sollen — und
warte auf die Antwort, bevor irgendetwas in den Graphen wandert.

---

## Regeln

- **Nichts erfinden**, keine Kante behaupten, die inhaltlich nicht trägt.
- **Nichts löschen.** Ein widerlegter Node bekommt einen datierten `⛔ WIDERLEGT`-Marker
  mit Gegenbeleg, der alte Absatz bleibt durchgestrichen stehen. Auch das ist ein
  Vorschlag, keine Ausführung.
- **Kein Ziel „möglichst viele Kanten".** Null Waisen ist sinnvoll, sechs Kanten pro
  Node erzeugen Rauschen, das die Suche verschlechtert.
- **Nicht mehr als einen Anlauf je Kandidat.** Was nach einer Prüfung unklar bleibt,
  wird `UNKLAR` und wandert zum Menschen, statt weiter bearbeitet zu werden.
