#!/usr/bin/python
# -*- coding:utf-8 -*-
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, by, value):
        return self._driver.find_element(by, value)
