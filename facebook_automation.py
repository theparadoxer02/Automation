from selenium import webdriver
from selenium.webdriver.common.keys import Keys


user_name = input('Enter the User Name:  ')
pass_word = input('Enter the password:   ')


browser = webdriver.Firefox()
browser.get('http://www.facebook.com')
email = browser.find_element_by_name('email')
password = browser.find_element_by_name('pass')

email.send_keys(user_name)
password.send_keys(pass_word)


login = login = browser.find_element_by_css_selector('#u_0_w')


login.click()

option_point = browser.find_element_by_css_selector('#userNavigationLabel')

option_point.click()

browser.switchTo().window(tabs.get());

#logout = browser.find_element_by_className('_54nh')


logout.click()