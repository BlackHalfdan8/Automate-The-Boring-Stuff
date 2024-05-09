# regexSearch.py - Searches a user-provided folder path for a user-provided regex pattern
#                  and prints the results to the screen.

import os, re

def search_files_in_folder(folder_path, regex_pattern):
    # Check if the folder path exists
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        return

    # Get a list of all files in the folder
    files_in_folder = os.listdir(folder_path)

    # Iterate through each file and search for the pattern
    for file_name in files_in_folder:
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as file:
                for line in file:
                    if re.search(regex_pattern, line):
                        print(f"Match found in {file_name}: {line.strip()}")

# Get user input for folder path and regular expression pattern
folder_path = input("Enter the folder path: ")
regex_pattern = input("Enter the regular expression pattern to search: ")

# Call the search_files_in_folder function
search_files_in_folder(folder_path, regex_pattern)
