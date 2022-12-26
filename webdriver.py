from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
load_dotenv('./.env')
user = os.environ['USERNAME']
passw = os.environ['PASSWORD']
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
import time

driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)

driver.get('https://instagram.com/')

#login
time.sleep(20)
username=driver.find_element("css selector", "input[name='username']")
password=driver.find_element("css selector", "input[name='password']")
username.clear()
password.clear()
username.send_keys(user)
password.send_keys(passw)
login = driver.find_element("css selector", "button[type='submit']").click()