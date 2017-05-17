'''fill your email and password and run the file'''
from selenium import webdriver 
import time
def fb_login():
    browser=webdriver.Firefox()
    browser.get('https://facebook.com')
    time.sleep(1)
    user=browser.find_element_by_css_selector('#email')
    user.send_keys('***********')
    password=browser.find_element_by_css_selector('#pass')
    password.send_keys('**********')
    login=browser.find_element_by_css_selector('#u_0_l')
    login.click()
fb_login()
#print("yogendra")
