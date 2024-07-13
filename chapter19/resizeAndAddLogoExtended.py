import os
from PIL import Image

# Constants for the logo and resizing
LOGO_FILENAME = 'catlogo.png'
EXTENSIONS = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
NEW_WIDTH = 300
NEW_HEIGHT = 300

# Load the logo image
logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

# Create a new directory to save modified images
os.makedirs('withLogo', exist_ok=True)

# Loop over all files in the working directory
for filename in os.listdir('.'):
    # Check if the file is an image
    if any(filename.lower().endswith(ext) for ext in EXTENSIONS) and filename != LOGO_FILENAME:
        im = Image.open(filename)
        width, height = im.size

        # Resize the image
        if width > NEW_WIDTH or height > NEW_HEIGHT:
            print(f'Resizing {filename}...')
            im = im.resize((NEW_WIDTH, NEW_HEIGHT))

        # Add the logo
        if im.width >= 2 * logoWidth and im.height >= 2 * logoHeight:
            print(f'Adding logo to {filename}...')
            im.paste(logoIm, (im.width - logoWidth, im.height - logoHeight), logoIm)

        # Save the changes
        im.save(os.path.join('withLogo', filename))

print('All images processed.')
