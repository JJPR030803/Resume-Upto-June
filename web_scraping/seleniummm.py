from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')
linkElem = browser.find_element(by=By.LINK_TEXT,value='Read Online for Free')
linkElem.click()