---
description: Ertrag der Sitzung ins Tageslog des Graphen sichern
---

# Session-Tagebuch

Sichere den Ertrag dieser Sitzung **jetzt** ins Tageslog des Graphen — dieselbe
Datei und dasselbe Format, das der `SessionEnd`/`PreCompact`-Hook schreibt.

Nutze das, wenn du mitten in einer langen Sitzung sichern willst, bevor kompaktiert
wird, oder wenn der Hook nachweislich nicht gelaufen ist.

---

## Ziel

`$BRAIN_ROOT/.daily/YYYY-MM-DD.md` (heutiges Datum). Ist `BRAIN_ROOT` nicht gesetzt,
melde das und schreibe nichts — rate keinen Pfad.

**Angehängt, nie überschrieben.** Mehrere Einträge pro Tag sind der Normalfall;
existiert die Datei nicht, beginne sie mit `# Daily Log: YYYY-MM-DD`.

## STEP 1: Ertrag bestimmen

Nicht den Ablauf der Sitzung, sondern was in vier Wochen noch trägt:

- Welche Entscheidungen wurden getroffen, und warum diese statt der Alternative?
- Was hat der User korrigiert? Korrekturen sind das wertvollste Material —
  aus ihnen werden `feedback`-Nodes.
- Welches Verhalten war anders als erwartet, mit welchem Beleg?
- Was ist offen geblieben?

Steht nichts davon an, ist „keine neuen Erkenntnisse" das richtige Ergebnis. Dann
nichts schreiben.

## STEP 2: Eintrag anhängen

Exakt dieses Format — der Compiler liest es, eine eigene Struktur bricht ihn:

```markdown
### Session (HH:MM)

**Context:** <ein bis zwei Sätze, worum es ging und was dabei herauskam>

**Key Exchanges:**
- <die Wendepunkte des Gesprächs, nicht jeder Schritt>

**Decisions Made:**
- <Entscheidung + Grund. Was verworfen wurde, gehört dazu>

**Lessons Learned:**
- <belegte Einzelaussagen. Das ist der Rohstoff für `claim`- und `feedback`-Nodes>

**Action Items:**
- <offene Punkte, mit dem, was sie blockiert>
```

## STEP 3: Vorlegen

Zeige den Eintrag, bevor du ihn schreibst, und korrigiere auf Zuruf.

---

## Regeln

- **Nichts erfinden.** Nur was tatsächlich vorkam. Kein Beleg → nicht schreiben.
- **Kontextfrei formulieren.** Der Compiler sieht diese Sitzung nicht, nur den Text.
- **Keine Secrets, keine personenbezogenen Daten.** Zugänge über ihren Ort nennen,
  nie über ihren Wert.
- **Keine Nodes schreiben.** Dieser Befehl füllt nur das Rohlog. Typisierte Nodes
  entstehen im Compile (`/consolidate` oder der nächtliche Lauf).
- Doppelt erfasst ist unkritisch: Der Compile dedupliziert gegen den Bestand.
