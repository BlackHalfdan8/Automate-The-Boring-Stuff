#! python3
# selectiveCopy.py - Asks user for input on which source folder to walk
# which destination folder to write to and which file extension to copy.

import os
import shutil

def selective_copy(source_folder, dest_folder, file_extension):
    # Ensure destination folder exists
    os.makedirs(dest_folder, exist_ok=True)
    
    # Walk through the source folder
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.endswith(file_extension):
                # Construct full file path
                file_path = os.path.join(foldername, filename)
                
                # Copy the file to the destination folder
                shutil.copy(file_path, dest_folder)
                print(f'Copied {file_path} to {dest_folder}')

# Example usage
source_folder = input("Enter the source folder path: ")
dest_folder = input("Enter the destination folder path: ")
file_extension = input("Enter the file extension to copy (e.g., .pdf, .jpg): ")

selective_copy(source_folder, dest_folder, file_extension)
