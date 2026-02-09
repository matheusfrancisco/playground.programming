#!/bin/bash
# pass input file as first argument
if [ -z "$1" ]; then
  echo "Usage: $0 <input_file>"
  exit 1
fi
input_file="$1"
echo "Input file: $input_file"
g++ -Werror -std=c++17 -O2 -lm $input_file -o main

echo "Running the program..."
./main

echo "Cleaning up..."
rm -f main

