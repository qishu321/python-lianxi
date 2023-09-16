import requests
from lxml import etree
from os import makedirs
from os.path import exists

DIST_DIR = 'dist'
exists(DIST_DIR) or makedirs(DIST_DIR)

urls = 'http://www.netbian.com/meinv/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41'
}

def Page(url):
    r = requests.get(url, headers=headers)
    r.encoding = 'gbk'  # 设置编码格式
    html = etree.HTML(r.text)
    return html

def Url(page):
    index_url = f'{urls}index_{page}.htm'
    return Page(index_url)

def extract_movie_info(movie):
    title = movie.xpath('//*[@id="main"]//ul//li//a//img//@alt')
    '//*[@id="main"]/div[4]/ul/li[1]/a'
    '//*[@id="main"]/div[4]/ul/li[1]/a/img'
    img = movie.xpath('//*[@id="main"]//ul//li/a/img//@src')
    print(img)
    return title, img

def main():
    for i in range(2, 11):
        lists = Url(i)
        titles, img_links = extract_movie_info(lists)
        print(titles,img_links)
        for title, img_link in zip(titles, img_links):
            try:
                response = requests.get(img_link, headers=headers)
                with open(f'{DIST_DIR}/{title}.jpg', 'wb') as f:
                    f.write(response.content)
                print(f'Downloaded: {DIST_DIR}/{title}')
            except Exception as e:
                print(f'Failed to download: {DIST_DIR}/{title} - {e}')


if __name__ == '__main__':
    main()
