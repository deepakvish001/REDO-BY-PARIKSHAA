#!/usr/bin/env bash
#
# Compile-check every committed solution.
#
# Solutions are stored exactly as they were submitted to the judge, which
# means the Java files are LeetCode snippets: no imports, and a class name
# that does not match the file name. Both are supplied by LeetCode's own
# harness, so this script reproduces that environment rather than rewriting
# the archive — a solution is judged on whether it compiles the way the
# judge compiled it.
#
# Usage: tools/check-solutions.sh
set -uo pipefail

cd "$(dirname "$0")/.."
BUILD=$(mktemp -d)
trap 'rm -rf "$BUILD"' EXIT

pass=0
fail=0
failed_files=()

record() {
  if [ "$1" -eq 0 ]; then
    pass=$((pass + 1))
  else
    fail=$((fail + 1))
    failed_files+=("$2")
    echo "FAIL  $2"
    sed 's/^/      /' "$3" | grep -v 'JAVA_TOOL_OPTIONS' | head -5
  fi
}

echo "── Java"
while IFS= read -r f; do
  [ -n "$f" ] || continue
  d=$(mktemp -d "$BUILD/XXXXXX")
  cls=$(grep -oE '(public +)?(final +)?class +[A-Za-z_][A-Za-z0-9_]*' "$f" | head -1 | awk '{print $NF}')
  cls=${cls:-Solution}
  {
    echo "import java.util.*;"
    echo "import java.io.*;"
    cat "$f"
  } > "$d/$cls.java"
  javac -nowarn -d "$d" "$d/$cls.java" 2>"$d/err"
  record $? "$f" "$d/err"
done < <(git ls-files '*.java')

echo "── C++"
while IFS= read -r f; do
  [ -n "$f" ] || continue
  err=$(mktemp)
  g++ -std=gnu++17 -fsyntax-only "$f" 2>"$err"
  record $? "$f" "$err"
done < <(git ls-files '*.cpp')

echo "── Python"
while IFS= read -r f; do
  [ -n "$f" ] || continue
  err=$(mktemp)
  python3 -m py_compile "$f" 2>"$err"
  record $? "$f" "$err"
done < <(git ls-files '*.py')

echo
echo "══ $pass passed, $fail failed"
if [ "$fail" -gt 0 ]; then
  printf 'Failing solutions:\n'
  printf '  %s\n' "${failed_files[@]}"
  exit 1
fi
