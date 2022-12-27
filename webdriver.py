from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
# from dotenv import load_dotenv
# load_dotenv('./.env')
# user = os.environ['USERNAME']
# passw = os.environ['PASSWORD']
chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
chrome_options.add_experimental_option("detach", True)
import time

driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)
driver.maximize_window()

# driver.get('https://instagram.com/')

# #login
# time.sleep(15)
# username=driver.find_element("css selector", "input[name='username']")
# password=driver.find_element("css selector", "input[name='password']")
# username.clear()
# password.clear()
# username.send_keys(user)
# password.send_keys(passw)
# login = driver.find_element("css selector", "button[type='submit']").click()

# #save your login info?
# time.sleep(10)
# notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
# #turn on notif
# time.sleep(10)
# notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
# time.sleep(10)
# messages = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/a/div").click()

driver.get('https://www.instagram.com/direct/inbox/')

message = driver.find_element(By.CSS_SELECTOR, 'div._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9_._aba8._abcm').click()