# brain-kit

Vier Befehle für ein Gedächtnis aus Markdown-Nodes.

```
/plugin marketplace add neurawork-git/brain-starterkit
/plugin install brain-kit@brain-starterkit
```

Danach Sitzung neu starten — die Befehlsliste wird beim Start eingelesen.

## Voraussetzung

`BRAIN_ROOT` als **absoluter** Pfad in `~/.claude/settings.json`:

```json
{ "env": { "BRAIN_ROOT": "C:/Pfad/zu/deinem/vault" } }
```

Kein `~` im Wert. Fehlt die Variable, brechen die Befehle mit einer Meldung ab,
statt einen Pfad zu raten.

Der Vault muss der Konvention folgen — Skelett und Prüfskript liegen im
[`vault/`](../../vault/) dieses Repos, das Format erklärt
[Stufe 1](../../docs/stufe-1-konvention.md).

## Befehle

| Befehl | Aufgabe |
|---|---|
| `/primer` | Index, offene Entscheidungen, Projekt-Kontext und jüngste Arbeit laden |
| `/diary` | Ertrag der laufenden Sitzung ins Tageslog sichern |
| `/consolidate` | Unverarbeitete Tageslogs zu typisierten Nodes destillieren, Index nachziehen |
| `/daily-summary` | Tagesbericht aus Tageslog, Commits, Compile-Stand und offenen Entscheidungen |

## Was sie nicht tun

Entscheidungen werden nur vorgeschlagen und in `decisions/_queue.md` gehängt;
annehmen darf ein Mensch. Gelöscht wird nichts — Widerlegtes bekommt einen datierten
Marker mit Gegenbeleg.

`/diary` schreibt ausschließlich Rohmaterial, nie Nodes. Diese Trennung ist der
Grund, warum später nachvollziehbar bleibt, woher eine Aussage kommt.

## Änderungen

Nach jeder Änderung an diesem Plugin die `version` in
[`.claude-plugin/plugin.json`](.claude-plugin/plugin.json) hochsetzen. `/plugin update`
vergleicht die Version, nicht den Inhalt: Ohne Bump meldet es „already at the latest
version", und der Cache bleibt still veraltet.
