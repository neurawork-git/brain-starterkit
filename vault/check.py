"""Prüft einen Brain-Vault: Frontmatter, Pflichtfelder, Linkziele, Waisen.

    python check.py brain
    python check.py --selftest

Nur Standardbibliothek — kein pyyaml. Das Frontmatter wird flach gelesen
(key: value), weil die Konvention flach ist.
"""
import re
import sys
from pathlib import Path

PFLICHT = ("name", "description", "type", "tags", "date")
# Das unsichtbare Zeichen vor "?---" ist ein BOM: Dateien aus manchen
# Windows-Editoren beginnen damit, und ohne die Toleranz gilt so eine
# Datei faelschlich als "kein Frontmatter" — genau der stille Ausfall,
# den dieses Skript finden soll.
FM = re.compile(r"\A﻿?---\r?\n(.*?)\r?\n---", re.S)
LINK = re.compile(r"\[\[([^\]|#]+)")


def lies(pfad: Path) -> tuple[dict, set[str]]:
    """Frontmatter-Felder und Linkziele einer Datei. Kein Frontmatter -> ({}, links)."""
    text = pfad.read_text(encoding="utf-8")
    ziele = {z.strip().split("/")[-1] for z in LINK.findall(text)}
    treffer = FM.match(text)
    if not treffer:
        return {}, ziele
    felder = {}
    for zeile in treffer.group(1).splitlines():
        if ":" in zeile and not zeile.startswith((" ", "\t", "#")):
            k, _, v = zeile.partition(":")
            felder[k.strip()] = v.strip()
    return felder, ziele


def pruefe(wurzel: Path) -> list[str]:
    dateien = sorted(p for p in wurzel.rglob("*.md") if not p.name.startswith("."))
    if not dateien:
        return [f"{wurzel}: keine .md-Dateien gefunden"]

    bekannt = {p.stem for p in dateien}
    befunde, ausgehend, eingehend = [], {}, set()

    for p in dateien:
        rel = p.relative_to(wurzel)
        felder, ziele = lies(p)
        if p.name in ("MEMORY.md", "INDEX.md") or p.parent.name == "templates":
            eingehend |= ziele  # Index zählt als Verweis-Quelle, nicht als Node
            continue
        if not felder:
            befunde.append(f"{rel}: kein Frontmatter — für Suche und Injektion unsichtbar")
            continue
        for feld in PFLICHT:
            if feld not in felder:
                befunde.append(f"{rel}: Feld '{feld}' fehlt")
        # Beide Schreibweisen gelten: "mein-node" und "claims/mein-node".
        # Die zweite ist die kg-Form aus beispiele/compiler-prompt.md.
        if felder.get("name") and felder["name"].split("/")[-1] != p.stem:
            befunde.append(f"{rel}: name '{felder['name']}' weicht vom Dateinamen ab")
        ausgehend[p.stem] = ziele
        eingehend |= ziele
        for ziel in ziele - bekannt:
            befunde.append(f"{rel}: toter Link [[{ziel}]]")

    for stem in ausgehend:
        if not ausgehend[stem] and stem not in eingehend:
            befunde.append(f"{stem}: Waise — weder ein- noch ausgehende Kante")
    return befunde


def selftest() -> None:
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        w = Path(tmp)
        gut = "---\nname: a\ndescription: x\ntype: claim\ntags: [t]\ndate: 2026-01-01\n---\nVerwandt: [[b]]\n"
        (w / "a.md").write_text(gut, encoding="utf-8")
        (w / "b.md").write_text(gut.replace("name: a", "name: b").replace("[[b]]", "[[a]]"), encoding="utf-8")
        assert pruefe(w) == [], pruefe(w)

        # kg-Form mit Typ-Praefix und eine Datei mit BOM gelten als gueltig
        (w / "f.md").write_text(gut.replace("name: a", "name: claims/f").replace("[[b]]", "[[a]]"), encoding="utf-8")
        (w / "g.md").write_text("﻿" + gut.replace("name: a", "name: g").replace("[[b]]", "[[a]]"), encoding="utf-8")
        assert pruefe(w) == [], pruefe(w)

        (w / "c.md").write_text("kein kopf\n", encoding="utf-8")
        (w / "d.md").write_text(gut.replace("name: a", "name: d").replace("[[b]]", "[[weg]]"), encoding="utf-8")
        (w / "e.md").write_text(gut.replace("name: a", "name: e").replace("Verwandt: [[b]]", "allein"), encoding="utf-8")
        meldungen = " | ".join(pruefe(w))
        assert "kein Frontmatter" in meldungen, meldungen
        assert "toter Link [[weg]]" in meldungen, meldungen
        assert "e: Waise" in meldungen, meldungen
    print("selftest ok")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "brain"
    if arg == "--selftest":
        selftest()
        raise SystemExit(0)
    treffer = pruefe(Path(arg))
    for zeile in treffer:
        print(zeile)
    print(f"\n{len(treffer)} Befund(e).")
    raise SystemExit(1 if treffer else 0)
