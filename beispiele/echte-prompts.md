# Echte Prompts, echte Treffer

Die Injektion aus Stufe 4 ist nur so gut wie ihre Trefferquote — und die ist
messbar. Grundlage ist ein **eingefrorenes Goldset**: echte Nutzer-Prompts aus
Sitzungsmitschriften, dahinter der Node, den die Suche hätte liefern müssen.

Unten eine Auswahl daraus, wörtlich übernommen inklusive Tippfehler. Genau so
kommen sie an. Prompts mit Kundenbezug, Zahlen aus Verträgen oder einem Schlüssel
im Text sind hier herausgenommen — im internen Goldset stehen sie, ein Prompt mit
einem API-Schlüssel wurde verworfen statt redigiert.

| Prompt | Erwarteter Node |
|---|---|
| Das ist eine extrem niedrige Skill Quote. | `skill-quote-pro-session-nicht-pro-toolcall` |
| Hm. Aber wieso werden skills nich tgezogen? brauchen wir explizitere "use whens" in den skill descriptio? | `nicht-gezogener-skill-ist-eher-coverage-loch-als-trigger-loch` |
| Nun wirklich verdächtig viele orphans, da stimtm was nicht im algorithmus | `obsidian-waise-ist-isoliert-nicht-ohne-eingehende-kante` |
| Ist der Verweis aufs Brain auch im Opencode hinterlegt? | `opencode-brain-anbindung` |
| Litllm errors on the stackit machine, please check | `litellm-ein-worker-serialisiert-die-gpu` |
| Na wir haben ne wildcard, gib mir die ip dann setze ichs | `wildcard-dns-deckt-namen-mit-kindrecord-nicht-ab` |
| Wir haben keinen public fork? Woher nimmst du das? | `fork-button-erbt-sichtbarkeit-privat-nur-als-mirror-klon` |
| Could the qwen 3.8 be able to read images directly? | `qwen38-27b-auf-vllm-liest-bilder` |
| Hat Dashlane irgendein cli oder api? | `dashlane-hat-keine-rest-api-fuer-vault-inhalte` |
| Hast du API Zugriff aufs Memberspot? | `memberspot-openapi-weicht-von-der-api-ab` |

## Was man daran sieht

**Prompts sind kurz, unvollständig und oft falsch geschrieben.** Keiner davon
nennt das Thema so, wie ein Node überschrieben wäre. „Nun wirklich verdächtig
viele orphans" trifft einen Node, in dessen Titel „orphan" gar nicht vorkommt —
er trifft ihn nur, weil das Wort in den `tags` steht.

**Deshalb ist das Tag-Feld die eigentliche Arbeit.** Schreib die Wörter hinein,
die jemand tippt, wenn er den Node braucht: Werkzeugnamen, Fehlersymptome,
Tätigkeiten, beide Sprachen. Nicht die Wörter, die den Node beschreiben.

**Zwei Sprachen in einem Satz sind der Normalfall**, nicht die Ausnahme.

## Die Messung

Gemessen wird gegen dieselbe Suchfunktion, die auch der Hook benutzt — nicht
gegen eine nachgebaute. Sonst misst man den Nachbau.

| Änderung | Recall@5 |
|---|---|
| Ausgangsstand | 0,56 |
| Body als zusätzliches Suchfeld, Abwertung von Rohquellen | 0,62 |
| 320 Nodes nachträglich getaggt | 0,68 |
| 55 neue Naben angelegt (verstopfen die besten fünf Plätze) | 0,64 |
| Naben abgewertet, damit die Einzelaussage vorn bleibt | 0,69 |

Die vierte Zeile ist die lehrreiche: Mehr gutes Material hat die Trefferquote
**gesenkt**. Naben sind breit und passen zu vielem, also verdrängen sie den
präzisen Node aus den besten fünf Plätzen. Sichtbar wurde das nur, weil vorher
gemessen wurde.

## Die Regel, ohne die die Messung wertlos ist

**Das Goldset wird nie an ein Messergebnis angepasst.** Wer eine Zeile ändert,
weil die Suche sie nicht trifft, misst ab dann die eigene Erwartung. Änderungen
nur mit Datum und Begründung.

## Selbst anlegen

Zwanzig Zeilen reichen für den Anfang. Nimm echte Prompts aus deinen letzten
Sitzungen — nicht ausgedachte, die sind zu gut formuliert — und schreib dahinter,
welchen Node du erwartet hättest. Dann friere die Liste ein.
