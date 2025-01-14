#!/bin/bash

# Loop through each file starting with "2017-"
for file in 2017-*.jpg; do
    # Check if the file exists to avoid errors
    if [[ -f "$file" ]]; then
        # Rename the file by appending "X_"
        mv "$file" "X_$file"
        echo "Renamed $file to X_$file"
    fi
done

echo "Batch rename complete."
