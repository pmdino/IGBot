from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time
load_dotenv('./.env')
user = os.environ['USERNAME']
passw = os.environ['PASSWORD']

chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=3024, 1964')
# chrome_options.add_argument("--headless")
chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36')

driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)
login = False
while login == False:
    try:
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
        notnowList = driver.find_elements(By.XPATH, "//button[contains(text(), 'Not Now')]")
        if (len(notnowList) > 0):
            notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        time.sleep(30)
        notnowList2 = driver.find_elements(By.XPATH, "//button[contains(text(), 'Not Now')]")
        if (len(notnowList2) > 0):
            notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        login = True
    except:
        print('uh oh')