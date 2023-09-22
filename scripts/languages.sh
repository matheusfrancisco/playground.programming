#!/usr/bin/env bash

set -euo pipefail

pushd "$(dirname "$0")/.." > /dev/null

FOLDERS=$(find . -name 'problem.md' | sed 's/problem.md//g' | sort)

for folder in $FOLDERS; do
    solutions="$(\
        find "$folder" \
            -regex \
            '.*\(clj\|cpp\|zig\|c\|rs\|py\)')"
    echo "$(echo "$solutions" | wc -w | sed 's/ //g') $folder"
done | sort -nr

popd  > /dev/null
