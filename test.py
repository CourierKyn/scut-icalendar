import selenium
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import hashlib
import requests
import os
browser = selenium.webdriver.Safari()
wait = WebDriverWait(browser, 10)
browser.set_window_size(1400, 900)


def login():
    browser.get('http://xsweb.scuteo.com/default2.aspx')
    user_name = wait.until(
        expected_conditions.presence_of_element_located((by.ID, 'txtUserName'))
    )
    password = wait.until(
        expected_conditions.presence_of_element_located((by.ID, 'TextBox2'))
    )
    code = wait.until(
        expected_conditions.presence_of_element_located((by.ID, 'txtSecretCode'))
    )
    code_image = wait.until(
        expected_conditions.presence_of_element_located((by.ID, 'icode'))
    )
    button = wait.until(
        expected_conditions.element_to_be_clickable((by.ID, 'Button1'))
    )
    user_name.send_keys('***********')
    password.send_keys('**********')


def download_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        print(response.status_code, 'from image')
        return None
    except requests.RequestException:
        print('RequestException from image')
        return None


def save_image(content):
    path = hashlib.md5(content).hexdigest() + '.' + 'jpg'
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(content)


def main():
    login()


if __name__ == '__main__':
    main()
