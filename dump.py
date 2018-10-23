from selenium import webdriver
browser = webdriver.Firefox()
# browser.maximize_window()
browser.get('https://www.gmail.com')
email=browser.find_element_by_xpath('//*[@id="identifierId"]')
email.send_keys('pankajgoyal125@gmail.com')
next=browser.find_element_by_xpath('//*[@id="identifierNext"]/content/span')
next.click()

browser.implicitly_wait(3)                              #wait_for 3 seconds

passwd=browser.find_element_by_name("password")
passwd.send_keys('mypassword')
next1=browser.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
next1.click()