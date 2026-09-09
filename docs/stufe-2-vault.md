# Stufe 2 — Der Vault

> **Ausführbar hier:** [`vault/`](../vault/) — Skelett, Vorlage, drei
> Beispiel-Nodes und [`vault/check.py`](../vault/check.py).

Ein Ordner, sonst nichts. Kein Server, keine Datenbank, kein Vektorindex — Markdown
in Git. Das ist keine Sparversion, sondern die Bedingung dafür, dass jedes Werkzeug
darauf zugreifen kann: Obsidian, `grep`, ein Agent, ein hochgeladener ZIP-Ordner in
einem ChatGPT-Projekt.

## Ordnerstruktur

```
vault/
  MEMORY.md          ← der Index. Nur Zeiger, nie Inhalt.
  claims/            ← belegte Einzelaussagen (der Großteil)
  feedback/          ← Arbeitsregeln aus Korrekturen
  references/        ← Zugänge, Instanzen, Zahlenwerke
  entities/          ← Kunden, Anbieter, Werkzeuge — die Naben
  projects/          ← laufende Arbeitsstände
  sources/           ← Rohmaterial, aus dem destilliert wurde
  templates/node.md  ← Vorlage
```

Ordner sind Bequemlichkeit, nicht Semantik: der Typ steht im Frontmatter. Verschiebe
eine Datei, und nichts bricht — die `[[wikilinks]]` sind namensbasiert, nicht
pfadbasiert.

## Loslegen

1. `vault/` an den Ort kopieren, wo du ihn versionierst.
2. Die drei Beispiel-Nodes lesen, dann löschen oder überschreiben.
3. Zwei Wochen lang nach jeder nennenswerten Arbeitseinheit einen Node schreiben.
4. `python vault/check.py <dein-vault>` laufen lassen, bevor du committest.

## Das Prüfskript

```
python check.py <dein-vault>   # prüft Frontmatter, Pflichtfelder, Links, Waisen
python check.py --selftest     # prüft das Skript selbst
```

Es meldet drei Klassen von Fehlern:

| Meldung | Bedeutung | Warum das teuer ist |
|---|---|---|
| `kein Frontmatter` / `Feld fehlt` | Datei hat keinen oder unvollständigen YAML-Kopf | Die Datei ist für jede Suche und jede Injektion **unsichtbar**. Sie sieht im Ordner gesund aus. |
| `toter Link` | `[[ziel]]` zeigt auf nichts | Entweder Tippfehler oder eine Lücke. Beides willst du sehen. |
| `Waise` | Node ohne ein- und ausgehende Kante | Existiert, wird nie gefunden. Der häufigste stille Ausfall. |

Tote Links sind nicht immer Fehler: ein Link auf einen noch ungeschriebenen Node ist
eine gültige Notiz an dich selbst. Waisen sind fast immer welche.

## Obsidian (optional)

Den Ordner als Vault öffnen. Die Graphenansicht zeigt sofort, was Stufe 1 abstrakt
behauptet: Nodes ohne Kanten liegen als isolierte Punkte am Rand. Das ist die
billigste Qualitätskontrolle, die es für diesen Ansatz gibt.

Obsidian gleicht `-` und `_` in Linkzielen **nicht** an. `[[mein-node]]` findet
`mein_node.md` nicht. Bleib bei Bindestrichen, überall.

## Verwendung ohne Agent

Ein ChatGPT-Projekt nimmt hochgeladene Dateien. Lade `MEMORY.md` plus die Nodes des
laufenden Themas hoch, nicht den ganzen Ordner — sonst gewinnt Menge über Relevanz.
Der Systemprompt aus Stufe 1 gilt unverändert.
