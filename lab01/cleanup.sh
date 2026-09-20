#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Usage: $0 <directory> [extension ...]"
    exit 1
fi

directory="$1"
shift

if [ ! -d "$directory" ]; then
    echo "Error: directory does not exist."
    exit 1
fi

if [ $# -eq 0 ]; then
    extensions=("tmp")
else
    extensions=("$@")
fi

count=0

for extension in "${extensions[@]}"; do
    while IFS= read -r -d '' file; do
        rm "$file"
        count=$((count + 1))
    done < <(find "$directory" -type f -name "*.$extension" -print0)
done

echo "Deleted files: $count"