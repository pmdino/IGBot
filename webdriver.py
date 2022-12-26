from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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

#save your login info?
time.sleep(10)
notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
#turn on notif
time.sleep(10)
notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()