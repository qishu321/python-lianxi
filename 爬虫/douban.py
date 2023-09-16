import requests
from bs4 import BeautifulSoup
import pandas as pd
import multiprocessing

urls = 'https://movie.douban.com/top250'
page = 10
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41'
}

def Page(url):
    response = requests.get(url=url, headers=headers)
    html = response.text
    return BeautifulSoup(html, 'html.parser')

def Url(page):
    index_url = f'{urls}?start={page}&filter='
    return Page(index_url)

def extract_movie_info(movie):
    title = movie.find("span", class_="title").text
    other = movie.find("span", class_="other").text.replace(' ', '')
    rating = movie.find('span', class_='rating_num').get_text()
    pingjia = movie.find('span', string=lambda s: s and s.endswith('人评价')).text.strip()
    inq_element = movie.find('span', class_='inq')
    inq = inq_element.text if inq_element else ""
    href = movie.find('a')['href']
    return title, rating, pingjia, inq, href

def main(page):
    data = []
    n = (page - 1) * 25
    lists = Url(n)
    movie_items = lists.findAll("div", class_="item")
    for movie in movie_items:
        movie_info = extract_movie_info(movie)
        data.append(movie_info)

    return data

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(1, page + 1)
    results = pool.map(main, pages)
    pool.close()
    pool.join()

    # 将所有页面的数据合并为一个列表
    all_data = [movie for page_data in results for movie in page_data]

    df = pd.DataFrame(all_data, columns=['电影名称', '评分', '人评价', '评语', '链接'])
    df.to_csv('douban_top250.csv', index=False)
