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
        driver.get('http://xsweb.scuteo.com/(ach3c545pkt1rh55y4fos0jt)/xs_main.aspx?xh=201636438964')
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


def select_xy(index):
    try:
        wait_table()
        time.sleep(1)
        wait_table()
        if 0 <= index < len(Select(driver.find_element_by_name('xy')).options):
            wait_zy()
            time.sleep(1)
            wait_zy()
            zy_options = [i.text for i in Select(driver.find_element_by_name('zy')).options]
            Select(driver.find_element_by_name('xy')).select_by_index(index)
            wait_zy()
            time.sleep(1)
            wait_zy()
            counter = 0
            while [i.text for i in Select(driver.find_element_by_name('zy')).options] == zy_options:
                counter += 1
                if counter == 10:
                    print(index)
                    return 0
                time.sleep(0.1)
            return 1
        else:
            return 0
    except:
        print(index)
        return 0


def select_zy(index):
    try:
        wait_zy()
        time.sleep(0.1)
        wait_zy()
        if 0 <= index < len(Select(driver.find_element_by_name('zy')).options):
            wait_kb()
            time.sleep(0.5)
            wait_kb()
            kb_options = [i.text for i in Select(driver.find_element_by_name('kb')).options]
            Select(driver.find_element_by_name('zy')).select_by_index(index)
            wait_kb()
            time.sleep(0.5)
            wait_kb()
            counter = 0
            while [i.text for i in Select(driver.find_element_by_name('kb')).options] == kb_options:
                counter += 1
                if counter == 5:
                    return 0
                time.sleep(0.1)
            return 1
        else:
            return 0
    except:
        return 0


def select_kb(index):
    try:
        wait_kb()
        wait_kb()
        if 0 < index < len(Select(driver.find_element_by_name('kb')).options):
            table = driver.find_element_by_id('Table6').text
            Select(driver.find_element_by_name('kb')).select_by_index(index)
            wait_table()
            counter = 0
            while driver.find_element_by_id('Table6').text == table:
                counter += 1
                if counter == 5:
                    return None
                time.sleep(0.1)
            return driver.page_source
    except:
        pass


def main():
    login()
    inquire()
    for i in range(6, 8):
        if select_xy(i):
            for j in range(0, 40):
                if select_zy(j):
                    for k in range(0, 20):
                        kb = select_kb(k)
                        if kb:
                            with open('{}{}{}.html'.format(i, j, k), 'w') as f:
                                f.write(kb)


if __name__ == '__main__':
    try:
        main()
    finally:
        driver.quit()
