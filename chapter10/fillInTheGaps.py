#! python3
# fillInTheGaps.py - Asks the user for the folder path to walk and prefix to find
# any gaps in numbering and re-names all the files to close those gaps sequentially.

import os
import re

def fill_gaps(folder, prefix):
    # List all files in the folder
    files = os.listdir(folder)
    
    # Create a regex pattern to match files with the given prefix and numbering
    pattern = re.compile(rf'^{prefix}(\d+)\.(txt|jpg|pdf|png|docx|etc)$')  # Adjust extensions as needed
    
    # Store the matched files with their numeric part
    matched_files = []
    for file in files:
        match = pattern.match(file)
        if match:
            matched_files.append((file, int(match.group(1))))
    
    # Sort files based on the numeric part
    matched_files.sort(key=lambda x: x[1])
    
    # Rename files to fill in the gaps
    current_number = 1
    for file, number in matched_files:
        if number != current_number:
            new_filename = f"{prefix}{str(current_number).zfill(len(str(number)))}{os.path.splitext(file)[1]}"
            print(f"Renaming {file} to {new_filename}")
            os.rename(os.path.join(folder, file), os.path.join(folder, new_filename))
        current_number += 1

# Example usage
folder = input("Enter the folder path: ")
prefix = input("Enter the file prefix: ")

fill_gaps(folder, prefix)
