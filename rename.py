import os
import re
from bs4 import BeautifulSoup

for i in os.listdir(os.getcwd()):
    if re.match(r'[0-9]+\.html$', i):
        with open(i) as f:
            soup = BeautifulSoup(f, 'lxml')
            name = soup.select('#kb > option[selected=selected]')[0].get_text()
        os.rename(i, name + '.html')
