from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
browser = wb.Firefox()
browser.get('https://inventwithpython.com')
try:
    elem = browser.find_element(by=By.CLASS_NAME,value='.cover-thumb')
    print('Found <%s> element with that class name' %(elem.tag_name))
except NoSuchElementException:
    print('Was not able to find an element')