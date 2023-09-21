#!/usr/bin/env bash

set -euo pipefail

FOLDERS=$1
LANGUAGES=$2
DOCKER_RUN_PREFIX=$3

for language in $LANGUAGES; do
    echo $language
    echo $DOCKER_RUN_PREFIX
    echo $FOLDERS
    echo "$DOCKER_RUN_PREFIX -e FOLDERS="$FOLDERS" "$language""
    $DOCKER_RUN_PREFIX -e FOLDERS="$FOLDERS" "$language"
done
