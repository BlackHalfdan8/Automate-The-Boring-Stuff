import os

# Constants for image extensions and threshold
EXTENSIONS = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
PHOTO_THRESHOLD = 5

def is_image_file(filename):
    return any(filename.lower().endswith(ext) for ext in EXTENSIONS)

def find_photo_folders(start_folder):
    for foldername, subfolders, filenames in os.walk(start_folder):
        num_photo_files = 0
        num_non_photo_files = 0

        for filename in filenames:
            if is_image_file(filename):
                num_photo_files += 1
            else:
                num_non_photo_files += 1

        # If the number of image files meets the threshold, print the folder path
        if num_photo_files >= PHOTO_THRESHOLD:
            abs_folder_path = os.path.abspath(foldername)
            print(f'{abs_folder_path} contains {num_photo_files} photo files')

# Specify the start folder
start_folder = '.'
find_photo_folders(start_folder)
