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

## Der schnellste Weg: die KI richtet sich selbst ein

Gib deinem Assistenten diesen Link und bitte ihn darum:

> Lies https://github.com/neurawork-git/brain-starterkit und richte mir das
> hier ein. Frag mich nach dem Ordner, in dem mein Gedächtnis liegen soll,
> und danach, welche Stufe zu meiner Umgebung passt. Erklär mir jeden
> Schritt, bevor du ihn machst.

Das funktioniert in Claude Code, in Cursor, in jedem Assistenten, der eine URL lesen
und Dateien anlegen kann. Er legt den Ordner an, trägt die Einstellungen ein und
sagt dir, was du selbst tun musst — Sitzung neu starten zum Beispiel, das kann er
nicht für dich.

Hat dein Assistent keinen Dateizugriff, etwa im Browser-Chat, dann bitte ihn stattdessen
darum, dir den Systemprompt aus Stufe 1 herauszusuchen und zu erklären. Auch dafür reicht
der Link.

Wenn du lieber selbst Hand anlegst, steht der Weg unten.

## Von Hand loslegen

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

Sitzung neu starten. Ab jetzt gibt es `/primer`, `/diary`, `/consolidate`,
`/daily-summary` und `/dream` in jedem Projekt.

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
| **5 — Dreaming** | Claude Code | [stufe-5-dreaming.md](docs/stufe-5-dreaming.md) | `/dream` aus demselben Plugin |
| **4 — Plugin** | Claude Code | [stufe-4-plugin.md](docs/stufe-4-plugin.md) | nicht enthalten, siehe unten |

**Die Regel über allem:** Eine Stufe ist erst sinnvoll, wenn die darunter sitzt. Ein
Hook, der vor jedem Prompt in einen Ordner ohne Konvention greift, injiziert
schneller Unsinn.

Fang bei Stufe 1 an, auch wenn du Claude Code hast. Wer die Konvention nicht von
Hand geübt hat, schreibt später Nodes, die niemand wiederfindet.

## Was hier nicht drin ist

**Stufe 4 ist beschrieben, nicht mitgeliefert.** Die automatische Injektion vor jedem
Prompt, das Capture am Sitzungsende und der nächtliche Destillierlauf laufen bei uns als
Hooks in einem eigenen Plugin, das nicht Teil dieser Veröffentlichung ist. Der Text
beschreibt die Mechanik so, dass man sie nachbauen kann, samt der Fehler, die wir dabei
gemacht haben.

Erreichbar ist trotzdem alles, nur nicht von selbst: `/diary` sichert, was der Hook
sonst automatisch sichert, `/consolidate` löst denselben Destillierlauf von Hand aus.

Bei Stufe 5 ist der Befehl enthalten, nur nicht unsere Orchestrierung. Unser
Refinement-Lauf verteilt die Rollen auf mehrere Agenten; `/dream` macht dasselbe der
Reihe nach in einer Sitzung.

## Ordner

- `docs/` — die fünf Stufentexte
- `vault/` — Ordnerskelett, Vorlage, drei Beispiel-Nodes, Prüfskript
- `plugins/brain-kit/` — das Plugin mit den vier Befehlen
- `beispiele/` — der wörtliche Compiler-Prompt und echte Nutzer-Prompts mit dem Node,
  den sie treffen sollten
- `scripts/scrub-check.sh` — prüft vor einem Push, dass keine eigenen Namen oder
  Zugangsdaten im Baum stehen. Die Begriffe kommen aus `.scrub-terms` (nicht
  eingecheckt) oder als Argumente, damit die Liste selbst nichts verrät.

## Lizenz

Apache License 2.0, siehe [LICENSE](LICENSE).

## Herkunft

Entstanden bei [Neurawork](https://neurawork.ai) im täglichen Betrieb. Die Zahlen in
den Texten sind an einem gewachsenen Graphen gemessen, nicht geschätzt.
