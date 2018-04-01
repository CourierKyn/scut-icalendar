import os
import re
from bs4 import BeautifulSoup
import pypinyin
'''for i in os.listdir(os.getcwd()):
    if re.match(r'.+\.ics$', i):
        pinyin = ''
        for j in pypinyin.lazy_pinyin(i.rsplit('.', 1)[0]):
            pinyin += j
        os.rename(i, pinyin + '.ics')'''
'''for i in os.listdir(os.getcwd()):
    if re.match(r'[0-9]+\.html$', i):
        with open(i) as f:
            soup = BeautifulSoup(f, 'lxml')
            name = soup.select('#kb > option[selected=selected]')[0].get_text()
        os.rename(i, name + '.html')'''
for i in os.listdir(os.getcwd()):
    if re.match(r'.+\.html$', i):
        pinyin = ''
        for j in pypinyin.lazy_pinyin(i.rsplit('.', 1)[0]):
            pinyin += j
        pinyin = pinyin.replace('(', '.')
        pinyin = pinyin.replace(')', '.')
        pinyin = pinyin.replace('（', '.')
        pinyin = pinyin.replace('）', '.')
        print('* [{}](https://github.com/CourierKyn/scut-icalendar/releases/download/v3.0/{})\n'.format(i.rsplit('.', 1)[0], (pinyin + '.ics').replace('..', '.')))
