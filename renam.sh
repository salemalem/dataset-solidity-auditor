#!/bin/bash

# Set maximum filename length
MAX_LENGTH=10

# Loop through all files in the current directory
for file in *; do
    # Check if the file is a regular file
    if [ -f "$file" ]; then
        # Get the file extension
        extension="${file##*.}"
        # Get the filename without the extension
        filename="${file%.*}"
        # Truncate the filename to the maximum length
        new_filename="${filename:0:$MAX_LENGTH}.${extension}"
        # Rename the file
        mv -v "$file" "$new_filename"
    fi
done