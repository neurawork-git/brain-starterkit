# Brain-Starterkit

Ein Gedächtnis für KI-Assistenten, das aus nichts weiter besteht als Markdown-Dateien
in einem Ordner. Kein Vektorindex, keine Datenbank, kein Dienst.

Das ist kein Konzeptpapier: Die Befehle in diesem Repo sind die, die wir selbst im
Alltag benutzen, nicht für die Weitergabe nachgebaute Fassungen.

## Die Idee in drei Sätzen

Wissen liegt als Ordner voller Markdown-Dateien. Eine Datei ist eine belegte Aussage,
mit YAML-Kopf und `[[wikilinks]]` auf verwandte Dateien. Der Assistent liest daraus
vor jeder Antwort den passenden Ausschnitt.

Der Unterschied zu „Notizen, die eine KI durchsuchen kann": Das Wissen wird nicht
abgerufen, es ist präsent. Ob der Assistent daran denkt nachzuschauen, ist keine
Variable mehr.

## Sofort loslegen

```bash
git clone https://github.com/neurawork-git/brain-starterkit
cp -r brain-starterkit/vault ~/mein-brain
```

In `~/.claude/settings.json`, absoluter Pfad, **kein `~`**:

```json
{
  "autoMemoryDirectory": "C:/Pfad/zu/mein-brain",
  "env": { "BRAIN_ROOT": "C:/Pfad/zu/mein-brain" }
}
```

Dann die Befehle installieren:

```
/plugin marketplace add neurawork-git/brain-starterkit
/plugin install brain-kit@brain-starterkit
```

Sitzung neu starten. Ab jetzt gibt es `/primer`, `/diary`, `/consolidate` und
`/daily-summary` in jedem Projekt.

Ohne Claude Code funktioniert die unterste Stufe trotzdem: Der Systemprompt in
[docs/stufe-1-konvention.md](docs/stufe-1-konvention.md) macht jedes Web-LLM
mitspielfähig, ganz ohne Dateizugriff.

## Die Stufen

Jede funktioniert allein. Höhere ersetzen die tieferen nicht, sie automatisieren sie.

| Stufe | Umgebung | Text | Ausführbar |
|---|---|---|---|
| **1 — Konvention** | jedes Web-LLM, ohne Dateizugriff | [stufe-1-konvention.md](docs/stufe-1-konvention.md) | Systemprompt zum Kopieren |
| **2 — Vault** | alles mit Dateizugriff, auch Obsidian | [stufe-2-vault.md](docs/stufe-2-vault.md) | [`vault/`](vault/) samt [`check.py`](vault/check.py) |
| **3 — Befehle** | Claude Code | [stufe-3-befehle.md](docs/stufe-3-befehle.md) | [`plugins/brain-kit/`](plugins/brain-kit/) |
| **4 — Plugin** | Claude Code | [stufe-4-plugin.md](docs/stufe-4-plugin.md) | nicht enthalten, siehe unten |
| **5 — Dreaming** | Claude Code, ab ~200 Nodes | [stufe-5-dreaming.md](docs/stufe-5-dreaming.md) | nicht enthalten, siehe unten |

**Die Regel über allem:** Eine Stufe ist erst sinnvoll, wenn die darunter sitzt. Ein
Hook, der vor jedem Prompt in einen Ordner ohne Konvention greift, injiziert
schneller Unsinn.

Fang bei Stufe 1 an, auch wenn du Claude Code hast. Wer die Konvention nicht von
Hand geübt hat, schreibt später Nodes, die niemand wiederfindet.

## Was hier nicht drin ist

**Stufe 4 und 5 sind beschrieben, nicht mitgeliefert.** Die automatische Injektion vor
jedem Prompt, das Capture am Sitzungsende und der nächtliche Destillierlauf laufen bei
uns als Hooks in einem eigenen Plugin, das nicht Teil dieser Veröffentlichung ist.
Die beiden Texte beschreiben die Mechanik so, dass man sie nachbauen kann, samt der
Fehler, die wir dabei gemacht haben.

`/consolidate` ist der Handgriff, der denselben Destillierlauf von Hand auslöst. Damit
ist auch ohne Hooks alles erreichbar, nur eben nicht von selbst.

## Ordner

- `docs/` — die fünf Stufentexte
- `vault/` — Ordnerskelett, Vorlage, drei Beispiel-Nodes, Prüfskript
- `plugins/brain-kit/` — das Plugin mit den vier Befehlen
- `beispiele/` — der wörtliche Compiler-Prompt und echte Nutzer-Prompts mit dem Node,
  den sie treffen sollten

## Herkunft

Entstanden bei [Neurawork](https://neurawork.ai) im täglichen Betrieb. Die Zahlen in
den Texten sind an einem gewachsenen Graphen gemessen, nicht geschätzt.
