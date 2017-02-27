from selenium import webdriver
from selenium.webdriver.common.keys import Keys


user_name = input('Enter the User Name:  ')
pass_word = input('Enter the password:   ')

browser = webdriver.Firefox()
browser.get('http://www.gmail.com')


email = browser.find_element_by_name('Email')           #email_element selection
email.send_keys(user_name)                              

browser.implicitly_wait(3)                              #wait_for 3 seconds

next_step  = browser.find_element_by_name('signIn')     #signin_elemet selection
next_step.click()


password = browser.find_element_by_name('Passwd')       #passsword element selection
password.send_keys(pass_word)

sign_in =  browser.find_element_by_css_selector('#signIn')  #sign_in selection
sign_in.click()

browser.implicitly_wait(200)                              #wait for 5 seconds

compose = browser.find_element_by_css_selector('.T-I-KE')   

compose.click()

browser.implicitly_wait(200)


to = browser.find_element_by_name('to')
subject = browser.find_element_by_name('subjectbox')
text = browser.find_element_by_class_name('Am Al editable LW-avf')

to.send_keys(user_name)
subject.send_keys('Testing')
text.send_keys('dekha beta')

send = browser.find_element_by_css_selector('#\:o2')
send.click()