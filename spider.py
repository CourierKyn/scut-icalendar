# encoding=utf-8
import requests
import re
import time
import random
from bs4 import BeautifulSoup
start_page = 'http://www.scut.edu.cn/new/'
global real_save
real_save = []


def get(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        print(response.status_code, 'from', url)
    except requests.RequestException:
        print('RequestException from', url)


def parse(html, url):
    try:
        soup = BeautifulSoup(html, 'lxml')
        for i in soup.find_all('a'):
            link = i.get('href')
            if link:
                if 'http' not in link:
                    link = str(re.match(r'https?://[^/]+', url).group()) + link
            yield link
    except:
        print('Exception')


def main(url):
    global real_save
    save = list(parse(get(url), url))
    for i in save:
        if i not in real_save:
            print(i)
    print('--------------------------------------------------------------------')
    real_save.extend(save)
    return save


if __name__ == '__main__':
    for i in main(start_page):
        main(i)
