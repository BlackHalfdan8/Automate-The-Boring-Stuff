import requests
from bs4 import BeautifulSoup
import sys

if len(sys.argv) < 2:
    print("Usage: python link_verification.py <url>")
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a', href=True)

def check_link(link_url):
    try:
        response = requests.head(link_url, allow_redirects=True)
        if response.status_code == 200:
            print(f'Link OK: {link_url}')
        else:
            print(f'Broken link: {link_url} (Status code: {response.status_code})')
    except requests.RequestException as e:
        print(f'Error checking link: {link_url} ({e})')

for link in links:
    link_url = link['href']
    if not link_url.startswith(('http:', 'https:')):
        link_url = requests.compat.urljoin(url, link_url)
    check_link(link_url)
