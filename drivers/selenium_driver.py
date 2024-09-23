from selenium import webdriver
from selenium.webdriver.chrome.service import Service

selenium_driver = None

def selenium_start():
    global selenium_driver
    if selenium_driver is None:
        # service = Service("C:\\Program Files\\chromedriver-win64\\chromedriver.exe")
        service = Service("C:\\Dropbox\\Tools\\Google\\chromedriver-win64\\chromedriver.exe")
        selenium_driver = webdriver.Chrome(service=service)
        print("Selenium session started:", selenium_driver)
    return selenium_driver

def selenium_stop():
    global selenium_driver
    if selenium_driver is not None:
        selenium_driver.quit()
        selenium_driver = None
        print("Selenium session stopped.")
