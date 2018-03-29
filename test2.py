import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import time
driver = selenium.webdriver.Chrome()
wait = WebDriverWait(driver, 10)


def login():
    try:
        driver.get('http://xsweb.scuteo.com/(gzhz2a45gq5l4r45kre24xu3)/xs_main.aspx?xh=201636438964')
    except:
        login()


def inquire():
    try:
        button1 = wait.until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#headDiv > ul > li:nth-child(6) > a > span'))
        )
        button2 = driver.find_element(By.CSS_SELECTOR, '#headDiv > ul > li:nth-child(6) > ul > li:nth-child(1) > a')
        button1.click()
        button2.click()
    except:
        inquire()


def wait_table():
    try:
        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_elements(By.TAG_NAME, 'iframe')[0])
        wait.until(expected_conditions.presence_of_element_located((By.ID, 'Table6')))
    except:
        wait_table()


def wait_zy():
    try:
        wait.until(expected_conditions.presence_of_element_located((By.NAME, 'zy')))
    except TimeoutError:
        wait_zy()


def wait_kb():
    try:
        wait.until(expected_conditions.presence_of_element_located((By.NAME, 'kb')))
    except TimeoutError:
        wait_kb()


def select(xy_index, zy_index, kb_index):
    zy_options = [i.text for i in Select(driver.find_element_by_name('zy')).options]
    Select(driver.find_element_by_name('xy')).select_by_index(xy_index)
    wait_zy()
    while [i.text for i in Select(driver.find_element_by_name('zy')).options] == zy_options:
        time.sleep(0.1)
    zy_options = [i.text for i in Select(driver.find_element_by_name('zy')).options]

    kb_options = [i.text for i in Select(driver.find_element_by_name('kb')).options]
    if 0 < zy_index < len(zy_options):
        Select(driver.find_element_by_name('zy')).select_by_index(zy_index)
        wait_kb()
        while [i.text for i in Select(driver.find_element_by_name('kb')).options] == kb_options:
            time.sleep(0.1)
        kb_options = [i.text for i in Select(driver.find_element_by_name('kb')).options]

    table = driver.find_element_by_id('Table6').text
    if 0 < kb_index < len(kb_options):
        Select(driver.find_element_by_name('kb')).select_by_index(kb_index)
        wait_table()
        while driver.find_element_by_id('Table6').text == table:
            time.sleep(0.1)
        return driver.page_source
    else:
        return None


def main():
    login()
    inquire()
    wait_table()
    print(select(0, 1, 1))


if __name__ == '__main__':
    try:
        main()
    finally:
        driver.quit()
