import requests
from lxml import etree
import os
import threading

DIST_DIR = 'dist2'
os.makedirs(DIST_DIR, exist_ok=True)

BASE_URL = 'https://www.fabiaoqing.com/bqb/lists/type/liaomei/page'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41'
}

def fetch_url(url):
    response = requests.get(url, headers=HEADERS)
    return response.text

def extract_movie_info(html):
    root = etree.HTML(html)
    titles = root.xpath('//*[@id="bqblist"]//div//div//img//@alt')
    img_links = root.xpath('//*[@id="bqblist"]//div//div//img//@data-original')
    return titles, img_links

def download_image(title, img_link):
    try:
        response = requests.get(img_link, headers=HEADERS)
        with open(f'{DIST_DIR}/{title}.jpg', 'wb') as f:
            f.write(response.content)
        print(f'Downloaded: {DIST_DIR}/{title}')
    except Exception as e:
        print(f'Failed to download: {DIST_DIR}/{title} - {e}')

def main():
    threads = []
    for page in range(2, 4):
        url = f'{BASE_URL}/{page}.html'
        html = fetch_url(url)
        titles, img_links = extract_movie_info(html)
        for title, img_link in zip(titles, img_links):
            desired_title = title.split(' - ')[0]
            thread = threading.Thread(target=download_image, args=(desired_title, img_link))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
