from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions

appium_driver = None

def appium_start():
    global appium_driver

    if appium_driver is None:
        cap: Dict[str, Any] = {
            'platformName': 'Android',
            'automationName': 'uiautomator2'
        }
        url = 'http://127.0.0.1:4723'
        appium_driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
        print("Appium session started:", appium_driver)
    return appium_driver

def appium_stop():
    global appium_driver
    if appium_driver is not None:
        appium_driver.quit()
        appium_driver = None
        print("Appium session stopped.")
