#!/usr/bin/env bash

set -euo pipefail

FOLDERS=$1
LANGUAGES=$2
DOCKER_RUN_PREFIX=$3
# make functions for each langauge if

for language in $LANGUAGES; do
    if [ "$language" = "clj" ]; then
      for folder in $FOLDERS; do
          [ -f "${folder}WRONG" ] && continue

          if [ "$(find "$folder" -name '*.clj' | wc -l)" -eq 1 ]; then
              echo "Running Clojure..." 
              echo "$folder" 
              cd "$folder" || exit 1
              if [ -f in.txt ]; then
                  clojure -M ./*.clj < in.txt > result-clj.txt
              else
                  clojure -M ./*.clj > result-clj.txt
              fi

              rm -rf './?'

              diff result-clj.txt out.txt

              cd - > /dev/null
          fi

          if [ "$(find "$folder" -name '*.cpp' | wc -l)" -eq 1 ]; then
              echo "Running Cpp..." 
              echo "$folder" 
              cd "$folder" || exit 1

              g++ -Werror -std=c++17 -O2 -lm ./*.cpp

              if [ -f in.txt ]; then
                  ./a.out < in.txt > result-cpp.txt
              else
                  ./a.out > result-cpp.txt
              fi

              rm -rf a.out

              diff result-cpp.txt out.txt

              cd - > /dev/null
          fi
          if [ "$(find "$folder" -name '*.py' | wc -l)" -eq 1 ]; then
              echo "Running Python..." 
              echo "$folder" 
              cd "$folder" || exit 1  

              if [ -f in.txt ]; then
                  python ./*.py < in.txt > result-py.txt
              else
                  python ./*.py > result-py.txt
              fi

              diff result-py.txt out.txt

              cd - > /dev/null
          fi

          if [ "$(find "$folder" -name '*.c' | wc -l)" -eq 1 ]; then
              echo "Running C..." 
              echo "$folder" 
              cd "$folder" || exit 1

              gcc -Werror -std=c99 -O2 -lm ./*.c

              if [ -f in.txt ]; then
                  ./a.out < in.txt > result-c.txt
              else
                  ./a.out > result-c.txt
              fi

              rm -rf a.out

              diff result-c.txt out.txt

              cd - > /dev/null
          fi

          if [ "$(find "$folder" -name '*.rs' | wc -l)" -eq 1 ]; then
              echo "Running Rust..." 
              echo "$folder" 
              cd "$folder" || exit 1

              rustc -o main ./*.rs

              if [ -f in.txt ]; then
                  ./main < in.txt > result-rs.txt
              else
                  ./main > result-rs.txt
              fi

              rm -rf main

              diff result-rs.txt out.txt

              cd - > /dev/null
          fi
        
      done
    fi
done
