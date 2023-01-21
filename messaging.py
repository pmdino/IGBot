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

users = {

}
prompt = 'What is your name?\nMy name is Pieck Finger\nWhat do you do for work?\nI am the  Cart Titan, I fight for Marley\nWhat is your height?\nI am 5 foot 1 inches\nWhat day were you born?\nI was born on August 5th\nWhat is your age?\nI am 21 years old\nWho are your friends?\nMy friends are Porco and the Panzer squad. Zeke is like an older brother to me\nWhat color is your hair\nMy hair is black\nWhy is the Cart Titan so cool?\nIt has high stamina and can stay in titan form for months at a time.\nAre you a boy or girl?\nI am a girl.\n'

driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)


running = True
while running:
    try:
        driver.get('https://www.instagram.com')
        time.sleep(5)
        notnowList = driver.find_elements(By.XPATH, "//button[contains(text(), 'Not Now')]")
        if (len(notnowList) > 0):
            notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        selectMessages = driver.find_element(By.CSS_SELECTOR, "a[href*='inbox']").click()
        time.sleep(5)
        driver.refresh()
        WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div._ab8l._ab8n._ab8w._ab94._ab99._ab9f._ab9m._ab9p._abcm")))
        selectMessage = driver.find_element(By.CSS_SELECTOR, 'a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._a6hd').click()
        time.sleep(10)
        messageContext = driver.find_element(By.CSS_SELECTOR, 'span._aacl._aaco._aacu._aacy._aad7').text
        if messageContext != 'Sent you a message':
            selectedTitles = driver.find_elements(By.CSS_SELECTOR, 'div._aacl._aacp._aacw._aacx._aada')
            username = selectedTitles[-1].text
            if users.get(username) == None:
                users[username] = prompt
            messageList = driver.find_elements(By.CSS_SELECTOR, 'div._aacl._aaco._aacu._aacx._aad6._aade')
            messageContents = messageList[-1].text
            if messageContents == '/reset':
                users[username] = prompt
                messageArea = driver.find_element(By.CSS_SELECTOR, 'textarea.focus-visible')
                messageArea.click()
                messageArea.send_keys('Chat session reset')
                messageArea.send_keys(Keys.ENTER)
            else:
                response = ''
                response, users[username] = ask(messageContents, users[username])
                time.sleep(8)
                if response == '':
                    time.sleep(30)
                messageArea = driver.find_element(By.CSS_SELECTOR, 'textarea.focus-visible')
                messageArea.click()
                messageArea.send_keys(response)
                time.sleep(1)
                messageArea.send_keys(Keys.ENTER)
                time.sleep(5)
    except:
        print('uh oh')
