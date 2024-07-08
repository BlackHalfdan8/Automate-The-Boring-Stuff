import requests
from bs4 import BeautifulSoup
import os
import sys

if len(sys.argv) < 2:
    print("Usage: python image_downloader.py <url>")
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

os.makedirs('images', exist_ok=True)

for img in img_tags:
    img_url = img.get('src')
    if not img_url:
        continue

    if not img_url.startswith(('http:', 'https:')):
        img_url = url + img_url

    img_filename = os.path.join('images', os.path.basename(img_url))

    img_response = requests.get(img_url)
    img_response.raise_for_status()

    with open(img_filename, 'wb') as img_file:
        for chunk in img_response.iter_content(8192):
            img_file.write(chunk)

    print(f'Downloaded {img_filename}')

print("All images downloaded successfully!")
