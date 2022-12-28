from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ai import *
import os
import openai
# from dotenv import load_dotenv
# load_dotenv('./.env')
# user = os.environ['USERNAME']
# passw = os.environ['PASSWORD']
chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
chrome_options.add_experimental_option("detach", True)
import time
prompt = 'What is your name?\nMy name is Pieck Finger\nWhat do you do for work?\nI am the  Cart Titan, I fight for Marley\nWhat is your height?\nI am 5 foot 1 inches\nWhat day were you born?\nI was born on August 5th\nWhat is your age?\nI am 21 years old\nWho are your friends?\nMy friends are Porco and the Panzer squad. Zeke is like an older brother to me\nWhat color is your hair\nMy hair is black\nWhy is the Cart Titan so cool?\nIt has high stamina and can stay in titan form for months at a time.\nAre you a boy or girl?\nI am a girl.'

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
running = True
while running:
    driver.get('https://www.instagram.com/direct/inbox/')
    time.sleep(10)
    WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div/div/div[2]/div[5]/div/a/div/div[1]/div/div[2]/div/span", "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/button")))
    if(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/button'))):
        selectRequest = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/button').click()
        selectRequestMessage = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[3]/div/div/div/div/a').click()
        time.sleep(3)
        selectYes = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/button').click()
    selectMessage = driver.find_element(By.CSS_SELECTOR, 'div._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9_._aba8._abcm').click()
    time.sleep(5)
    messageList = driver.find_elements(By.CSS_SELECTOR, 'div._aacl._aaco._aacu._aacx._aad6._aade')
    messageContents = messageList[-1].text
    response, prompt = ask(messageContents, prompt)
    time.sleep(5)
    messageArea = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    # time.sleep(15)
    messageArea.click()
    # time.sleep(15)
    messageArea.send_keys(response)
    messageArea.send_keys(Keys.ENTER)