#!/usr/bin/env bash
# Gate vor jedem Push in ein oeffentliches Repo: nichts Internes im Baum.
# Aufruf: scripts/scrub-check.sh [weitere begriffe ...]
# Exit 0 = sauber, 1 = Treffer (Ausgabe zeigt Datei und Zeile).
set -u

BEGRIFFE="falkensteg|stadtbau|khki|stolley|kloepfel|luettgens|tpit"
GEHEIM="BEGIN [A-Z ]*PRIVATE KEY|xox[baprs]-|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}"
[ $# -gt 0 ] && BEGRIFFE="$BEGRIFFE|$(printf '%s|' "$@" | sed 's/|$//')"

treffer=0
while IFS= read -r datei; do
  [ "$datei" = "scripts/scrub-check.sh" ] && continue
  # Ausgabe erst einfangen, dann pruefen: der Exit-Code einer Pipe waere der
  # des LETZTEN Befehls (sed/cut) und damit immer 0.
  fund=$(grep -niE "$BEGRIFFE" "$datei" 2>/dev/null || true)
  if [ -n "$fund" ]; then printf 'KUNDE  %s\n' "$datei"; printf '%s\n' "$fund" | cut -c1-100; treffer=1; fi
  fund=$(grep -niE "$GEHEIM" "$datei" 2>/dev/null || true)
  if [ -n "$fund" ]; then printf 'SECRET %s (Zeilen unterdrueckt)\n' "$datei"; treffer=1; fi
done < <(git ls-files)

if [ "$treffer" -eq 0 ]; then
  echo "sauber — $(git ls-files | wc -l) Dateien geprueft"
  exit 0
fi
echo
echo "Treffer gefunden. Nicht pushen, bevor sie weg sind."
exit 1
