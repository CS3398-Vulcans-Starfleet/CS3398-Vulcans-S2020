from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pg
import time

url = pg.prompt("Enter link to website.", "Website URL", "Link Here.")
username = pg.prompt("Enter Username or Email.", "Username/EMail", "Username or EMail.")
password = pg.prompt("Enter Password", "Password", "Password.")

driver = webdriver.Chrome()

def login(url,username,password):
   driver.get(url)
   driver.find_element_by_link_text('Sign in').click()
   time.sleep(1)
   driver.find_element_by_id('username').send_keys(username)
   driver.find_element_by_id("password").send_keys(password)
   driver.find_element_by_id("password").send_keys(Keys.ENTER)
   driver.find_element_by_link_text('A I').click()

login(url, username, password)