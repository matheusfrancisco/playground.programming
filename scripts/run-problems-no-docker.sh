#!/usr/bin/env bash

set -euo pipefail

FOLDERS=$1
LANGUAGES=$2
DOCKER_RUN_PREFIX=$3

for language in $LANGUAGES; do
    if [ "$language" = "clj" ]; then
      for folder in $FOLDERS; do
          [ -f "${folder}WRONG" ] && continue

          if [ "$(find "$folder" -name '*.clj' | wc -l)" -eq 1 ]; then
              echo "$folder" 
              cd "$folder" || exit 1
              echo "Running Clojure..." 
              if [ -f in.txt ]; then
                  clojure -M ./*.clj < in.txt > result-clj.txt
              else
                  clojure -M ./*.clj > result-clj.txt
              fi

              rm -rf './?'

              diff result-clj.txt out.txt

              cd - > /dev/null
          fi
        
      done
    fi
done
