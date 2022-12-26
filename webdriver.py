from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
import time

driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)

driver.get('https://images.google.com/')