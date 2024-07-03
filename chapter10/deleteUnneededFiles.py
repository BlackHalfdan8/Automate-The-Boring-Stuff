#! python3
# deleteUnneededFiles.py - Asks the user which folder to walk
# as well as what size threshold in bytes to send to the recycle bin.

import os
import send2trash

def delete_unneeded_files(folder, size_threshold):
    # Walk through the directory tree
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            
            # Check file size
            if os.path.getsize(file_path) > size_threshold:
                print(f'{file_path} is {os.path.getsize(file_path)} bytes')
                confirm = input(f'Do you want to send {file_path} to the trash? (yes/no): ')
                if confirm.lower() == 'yes':
                    send2trash.send2trash(file_path)
                    print(f'Sent {file_path} to the trash')

# Example usage
folder = input("Enter the folder path to search: ")
size_threshold = int(input("Enter the size threshold in bytes: "))

delete_unneeded_files(folder, size_threshold)
