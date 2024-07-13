from PIL import Image, ImageDraw, ImageFont
import os

# Constants for image size, font, and colors
WIDTH, HEIGHT = 400, 200
BACKGROUND_COLOR = 'white'
TEXT_COLOR = 'black'
FONT_SIZE = 40

# Load the font
try:
    font = ImageFont.truetype('arial.ttf', FONT_SIZE)
except IOError:
    font = ImageFont.load_default()

# Create a directory to save seating cards
os.makedirs('seating_cards', exist_ok=True)

# Read the guest list from a text file
with open('guest_list.txt') as file:
    guests = file.read().splitlines()

for guest in guests:
    # Create a blank image
    image = Image.new('RGBA', (WIDTH, HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(image)

    # Calculate the width and height of the text to center it
    text_width, text_height = draw.textsize(guest, font=font)
    text_x = (WIDTH - text_width) / 2
    text_y = (HEIGHT - text_height) / 2

    # Draw the guest's name on the image
    draw.text((text_x, text_y), guest, fill=TEXT_COLOR, font=font)

    # Save the image with a unique filename
    image.save(os.path.join('seating_cards', f'{guest}.png'))

print('All seating cards generated.')
