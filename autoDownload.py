from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as pg

download = pg.prompt("Enter what you want to download", "Download", "Here.")

driver = webdriver.Chrome()


def autoDownload(input):
    driver.get("https://www.google.com/")
    time.sleep(1)
    search = driver.find_element_by_name('q')
    search.send_keys(input)
    search.send_keys(Keys.ENTER)
    pg.hotkey('win', 'up')
    time.sleep(1)

    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('tab')
    pg.hotkey('enter')

    download = driver.find_element_by_link_text('Download Now')
    download.click()

autoDownload(download)
