#!/bin/bash

# If the file exists
if [ -f "audio.txt" ]; then
  while read -r file; do
    # Extract file name from each line
    file_name=$(basename "$file")
    # Determine the file type (m4a or flac) and rename it accordingly
    if [[ "$file_name" == *m4a ]]; then
      new_name=$(echo "$file_name" | sed -e 's/[^A-Za-z0-9._-]/_/g;s/ /_/g' | tr '[:upper:]' '[:lower:]')
      mv "$file_name" "$new_name"
    elif [[ "$file_name" == *flac ]]; then
      new_name=$(echo "$file_name" | sed -e 's/[^A-Za-z0-9._-]/_/g;s/ /_/g' | tr '[:upper:]' '[:lower:]')
      mv "$file_name" "$new_name"
    fi
  done < "audio.txt"
else
  echo "Error: audio.txt not found"
fi