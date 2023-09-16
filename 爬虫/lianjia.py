import time

import requests
from lxml import etree
from os import makedirs
from os.path import exists
import pandas as pd

DIST_DIR = 'dist2'
exists(DIST_DIR) or makedirs(DIST_DIR)

urls = 'https://sh.lianjia.com/ershoufang/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41'
}

def Page(url):
    r = requests.get(url, headers=headers)
    r.encoding = 'utf8'  # 设置编码格式
    html = etree.HTML(r.text)
    return html

def Url(page):
    index_url = f'{urls}/pg{page}dp1sf1bp0ep250'
    return Page(index_url)

def extract_movie_info(movie):
    region = movie.xpath('//*[@id="content"]//ul/li//div/div[2]/div/a[1]/text()')
    target = movie.xpath('//*[@id="content"]//ul/li//div/div[2]/div/a[2]/text()')
    houseIcon = movie.xpath('//*[@id="content"]//ul/li//div//div//div/text()')
    taxfree = movie.xpath('//*[@id="content"]//ul/li//div//div//span[@class="taxfree"]/text()')
    '//*[@id="content"]/div[1]/ul/li[1]/div[1]/div[6]/div[1]/span'
    price= movie.xpath('//*[@id="content"]//ul/li//div//div//div[1]/span/text()')
    aver_price= movie.xpath('//*[@id="content"]//ul/li//div//div//div[2]/span/text()')
    return region,target,houseIcon,taxfree,price,aver_price

def main():
    data = []  # 创建一个空的列表，用于存储提取的数据

    for i in range(0, 100):
        lists = Url(i)
        regions, targets, houseIcons, taxfrees, prices, aver_prices = extract_movie_info(lists)

        # 去掉 houseIcon 列表中的 ' - ' 和额外的空格
        houseIcons = [info.strip() for info in houseIcons if info.strip() != '-']
        houseIcons = [info for info in houseIcons if info]  # Remove empty strings
        print(houseIcons)
        for region, target, houseIcon, taxfree, price, aver_price in zip(regions, targets, houseIcons, taxfrees, prices,
                                                                         aver_prices):
            data.append([region, target, houseIcon, taxfree, price, aver_price])

        time.sleep(15)  # 添加15秒的延迟

    # 将数据转换为DataFrame
    df = pd.DataFrame(data, columns=["小区名称", "区域", "楼层详情", "房本满几年", "总价", "每平均价"])

    # 将DataFrame写入Excel文件
    df.to_excel(f'{DIST_DIR}/房屋信息.xlsx', index=False)




if __name__ == '__main__':
    main()

