from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.get('http://www.facebook.com')
email = browser.find_element_by_id('email') #ENTER EMAIL

#Don't be an idiot and save password in a text file 

# with open('test.txt', 'r') as myfile:   #Reads password from a text file 
#     Password=myfile.read().replace('\n', '')

password = browser.find_element_by_id('pass')

email.send_keys('abhimanyu98986@gmail.com')
password.send_keys('pankaj123')


login = browser.find_element_by_id('u_0_2')


login.click()

option_point = browser.find_element_by_id('pageLoginAnchor')

option_point.click()

browser.implicitly_wait(3)                              #wait_for 3 seconds

logout_button = browser.find_element_by_class_name('_54nc')

logout_button.click()

# browser.switchTo().window(tabs.get());

#logout = browser.find_element_by_className('_54nh')


# logout.click()