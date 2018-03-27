import selenium
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
browser = selenium.webdriver.Safari()
browser.set_window_size(1000, 500)
wait = WebDriverWait(browser, 10)


def login():
    browser.get('http://xsweb.scuteo.com/(20re51fzh5fh0nfdxfmbchbj)/xs_main.aspx?xh=201636438964')
    print('login')


def inquire():
    button1 = wait.until(
        expected_conditions.element_to_be_clickable((by.CSS_SELECTOR, '#headDiv > ul > li:nth-child(6) > a > span'))
    )
    button2 = browser.find_element(by.CSS_SELECTOR, '#headDiv > ul > li:nth-child(6) > ul > li:nth-child(1) > a')
    button1.click()
    button2.click()
    browser.switch_to.frame(browser.find_elements(by.TAG_NAME, 'iframe')[0])
    print('inquire')


def select():
    xy = wait.until(
        expected_conditions.presence_of_element_located((by.ID, 'xy')))
    zy = browser.find_element(by.ID, 'zy')
    kb = browser.find_element(by.ID, 'kb')
    xy_len = len(Select(xy).options)
    zy_len = len(Select(zy).options)
    kb_len = len(Select(kb).options)
    xy.send_keys(Keys.ENTER)
    for i in range(0, 10):
        xy.send_keys(Keys.ARROW_UP)
        time.sleep(1)
    xy.send_keys(Keys.ENTER)
    for i in range(0, xy_len):
        for j in range(0, zy_len):
            for k in range(1, kb_len):
                kb.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
                time.sleep(5)
                print(browser.page_source)
            zy = wait.until(
                expected_conditions.presence_of_element_located((by.ID, 'zy')))
            zy.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        xy = wait.until(
            expected_conditions.presence_of_element_located((by.ID, 'xy')))
        xy.send_keys(Keys.ARROW_DOWN, Keys.ENTER)


def main():
    login()
    inquire()
    select()


if __name__ == '__main__':
    try:
        main()
    finally:
        browser.close()
