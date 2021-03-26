#!/usr/bin/python
# -*- coding:utf-8 -*-
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    _driver: WebDriver = None
    _url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            caps = {
                "deviceName": "127.0.0.1:7555",
                "platformName": "Android",
                "platformVersion": "6.0.1",
                "browserName": "Browser",
                "automationName": "UiAutomator2",
                # "chromedriverExecutable": "C:\\webdriver\\chromedriver.exe",
                # "chromedriverExecutableDir": "C:\\webdriver",
                # "appPackage": "com.android.browser",
                # "appActivity": "com.android.browser.BrowserActivity",
                "noRest": True
            }
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        else:
            self._driver = driver
        self._driver.implicitly_wait(10)
        if self._url != "":
            self._driver.get(self._url)

    def wait_for_visible(self, locator, time=10):
        wait = WebDriverWait(self._driver, time)
        wait.until(EC.visibility_of_element_located(locator))

    def find(self, locator):
        self.wait_for_visible(locator)
        return self._driver.find_element(*locator)

    def click(self, locator):
        self.wait_for_visible(locator)
        self._driver.find_element(*locator).click()

    def send_keys(self, locator, value):
        self.find(locator).send_keys(value)

    def get_title(self):
        # WebDriverWait(self._driver, 10).until(EC.url_changes(self._url))
        return self._driver.title

    def quit(self):
        self._driver.quit()
