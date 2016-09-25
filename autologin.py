from selenium import webdriver 
import time
def fb_login():
    browser=webdriver.Firefox()
    browser.get('https://facebook.com')
    time.sleep(1)
    user=browser.find_element_by_css_selector('#email')
    user.send_keys('saiganesh6997@gmail.com')
    password=browser.find_element_by_css_selector('#pass')
    password.send_keys('saiganesh6997')
    login=browser.find_element_by_css_selector('#u_0_l')
    login.click()
fb_login()
