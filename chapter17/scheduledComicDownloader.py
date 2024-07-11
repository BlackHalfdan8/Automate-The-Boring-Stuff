#! python3
# scheduledComicDownloader.py - Downloads a web comic at a scheduled time every day.

import requests, os, bs4, schedule, time

def download_comic():
    url = 'https://xkcd.com/'  # Can be changed this to any other comic URL.
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
        return

    comicUrl = comicElem[0].get('src')
    if not comicUrl.startswith('http'):
        comicUrl = 'https:' + comicUrl

    print('Downloading image %s...' % comicUrl)
    res = requests.get(comicUrl)
    res.raise_for_status()

    os.makedirs('comics', exist_ok=True)
    with open(os.path.join('comics', os.path.basename(comicUrl)), 'wb') as imageFile:
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
    print('Comic downloaded.')

# Schedule the comic download every day at a specific time
schedule.every().day.at("08:00").do(download_comic)  # Set your desired time here

print('Comic downloader scheduled. Press Ctrl-C to quit.')

while True:
    schedule.run_pending()
    time.sleep(1)
