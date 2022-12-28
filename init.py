from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ai import *
import os
import openai
from dotenv import load_dotenv
load_dotenv('./.env')
user = os.environ['USERNAME']
passw = os.environ['PASSWORD']
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=3024, 1964')
# chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless")
chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36')
import time
prompt = 'What is your name?\nMy name is Pieck Finger\nWhat do you do for work?\nI am the  Cart Titan, I fight for Marley\nWhat is your height?\nI am 5 foot 1 inches\nWhat day were you born?\nI was born on August 5th\nWhat is your age?\nI am 21 years old\nWho are your friends?\nMy friends are Porco and the Panzer squad. Zeke is like an older brother to me\nWhat color is your hair\nMy hair is black\nWhy is the Cart Titan so cool?\nIt has high stamina and can stay in titan form for months at a time.\nAre you a boy or girl?\nI am a girl.'

driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)
# driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})
# driver.maximize_window()

driver.get('https://instagram.com/')

#login
time.sleep(15)
username=driver.find_element("css selector", "input[name='username']")
password=driver.find_element("css selector", "input[name='password']")
username.clear()
password.clear()
username.send_keys(user)
password.send_keys(passw)
login = driver.find_element("css selector", "button[type='submit']").click()

time.sleep(30)
notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
#turn on notif
time.sleep(30)