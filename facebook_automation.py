from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.get('http://www.facebook.com')
email = browser.find_element_by_name('ENTER EMAIL') #ENTER EMAIL

#Don't be an idiot and save password in a text file 

with open('test.txt', 'r') as myfile:   #Reads password from a text file 
    Password=myfile.read().replace('\n', '')

password = browser.find_element_by_name(Password)

email.send_keys(user_name)
password.send_keys(pass_word)


login = login = browser.find_element_by_css_selector('#u_0_w')


login.click()

option_point = browser.find_element_by_css_selector('#userNavigationLabel')

option_point.click()

browser.switchTo().window(tabs.get());

#logout = browser.find_element_by_className('_54nh')


logout.click()