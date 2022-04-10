from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json, time, os
from selenium import webdriver


'''Sets chrome options for Selenium.
Chrome options for headless browser is enabled.
'''
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_prefs = {}
chrome_options.experimental_options['prefs'] = chrome_prefs
chrome_prefs['profile.default_content_settings'] = {'images': 2}

driver = webdriver.Chrome(options=chrome_options)

with open('./YahooBaseballBot/yahoobaseballbot/cookies.json') as fp:
    data = json.load(fp)

driver.get('https://baseball.fantasysports.yahoo.com/')

for cookie in data:
    if 'sameSite' in cookie:
        if cookie['sameSite'] != 'Strict' and cookie['sameSite'] != 'Lax' and cookie['sameSite'] != 'None':
            cookie['sameSite'] = 'Strict'
    driver.add_cookie(cookie)

driver.set_window_size(3000,3000)
driver.get(os.environ.get('URL'))
driver.save_screenshot('image1.png')
driver.find_element(By.CSS_SELECTOR, '[value="Start Active Players"]').click()
driver.save_screenshot('image2.png')
driver.find_element(By.CLASS_NAME, 'start-active-week-button').click()
time.sleep(10)
driver.save_screenshot('image3.png')
driver.close()