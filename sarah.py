from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(profile)
browser = webdriver.Firefox()  # Creating an instance webdriver
for i in range(0,50):
    browser.get('https://sarahabasera.sarahah.com/')
    time.sleep(2)  # Let's the user see
    elem = browser.find_element_by_css_selector("#Text")
    elem.click()
    elem.clear()
    elem.send_keys("CODE - TEST")
    log = browser.find_element_by_css_selector("#Send")
    log.click()
    print("Text send sucessfull ! ")
