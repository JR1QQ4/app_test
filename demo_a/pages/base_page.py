#!/usr/bin/python
# -*- coding:utf-8 -*-
import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, by, value):
        return self._driver.find_element(by, value)

    def steps(self, path):
        with open(path) as f:
            steps = yaml.safe_load(f)
        element = None
        for step in steps:
            if "by" in step.keys():
                element = self.find(step["by"], step["value"])
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()
