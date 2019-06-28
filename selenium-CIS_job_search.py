#!/usr/bin/env python
# webdrivers -> https://chromedriver.storage.googleapis.com/index.html?path=2.36/

import time
from selenium import webdriver
__author__ = "James R. Aylesworth"
__copyright__ = "Copyright 2019"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "James R. Aylesworth"
__website__ = "https://b1nary0mega.github.io/"
__status__ = "Development"

# chrome webdriver must be installed -- see above ^^
browser = webdriver.Chrome('c:/users/ayleswoj/chromedriver.exe')  #!!! update path to webdriver location !!!#
browser.get('https://careers-cisecurity.icims.com')

time.sleep(3)  # wait for a few seconds for page to load

try:
    # agree to cookie use
    cookieAcceptButton = browser.find_element_by_css_selector(
        '#c-buttons > a.c-button')
    cookieAcceptButton.text
    cookieAcceptButton.click()
except Exception as e:
    print("Cookie Clicking error:: ", e)

time.sleep(5)  # wait for a few seconds before searching

# search for keyword listings
try:
    # iframes suck...
    browser.switch_to.frame("icims_content_iframe")
    # search for keyword
    keywordSearch2 = browser.find_element_by_xpath(
        "//*[@id='jsb_f_keywords_i']").send_keys("CERT")
    searchButton = browser.find_element_by_xpath(
        "//*[@id='jsb_form_submit_i']").click()
except Exception as e:
    print("Search Error :: ", e)
    browser.quit()  # kill the browser; this was last error...
