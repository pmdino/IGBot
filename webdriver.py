from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ai import ask
import time

chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=3024, 1964')
# chrome_options.add_argument("--headless")
chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36')


prompt = 'What is your name?\nMy name is Pieck Finger\nWhat do you do for work?\nI am the  Cart Titan, I fight for Marley\nWhat is your height?\nI am 5 foot 1 inches\nWhat day were you born?\nI was born on August 5th\nWhat is your age?\nI am 21 years old\nWho are your friends?\nMy friends are Porco and the Panzer squad. Zeke is like an older brother to me\nWhat color is your hair\nMy hair is black\nWhy is the Cart Titan so cool?\nIt has high stamina and can stay in titan form for months at a time.\nAre you a boy or girl?\nI am a girl.'

driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)


running = True
while running:
    driver.get('https://www.instagram.com')
    time.sleep(5)
    notnowList = driver.find_elements(By.XPATH, "//button[contains(text(), 'Not Now')]")
    if (len(notnowList) > 0):
        notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
    selectMessages = driver.find_element(By.CSS_SELECTOR, "a[href*='inbox']").click()
    time.sleep(5)
    WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div/div/div[2]/div[5]/div/a/div/div[1]/div/div[2]")))
    selectMessage = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/div/a').click()
    time.sleep(5)
    messageList = driver.find_elements(By.CSS_SELECTOR, 'div._aacl._aaco._aacu._aacx._aad6._aade')
    messageContents = messageList[-1].text
    response = ''
    response, prompt = ask(messageContents, prompt)
    time.sleep(5)
    if response == '':
        time.sleep(15)
    messageArea = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    messageArea.click()
    messageArea.send_keys(response)
    messageArea.send_keys(Keys.ENTER)