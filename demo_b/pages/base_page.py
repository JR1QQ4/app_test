#!/usr/bin/python
# -*- coding:utf-8 -*-
from time import sleep

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    _driver: WebDriver
    _black_list = [
        (MobileBy.XPATH, '//*[@text="确认"]'),
        (MobileBy.XPATH, '//*[@text="下次再说"]'),
        (MobileBy.XPATH, '//*[@text="确定"]'),
    ]
    _max_num = 3
    _error_num = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(locator))
            ele = self._driver.find_element(*locator)
            self._error_num = 0
            self._driver.implicitly_wait(10)
            return ele
        except Exception as e:
            self._driver.implicitly_wait(1)
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            for loc in self._black_list:
                ele_list = self._driver.find_elements(*loc)
                if len(ele_list) > 0:
                    ele_list[0].click()
                    return self.find(locator)
            raise e

    def find_presence(self, locator):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(locator))
        return self._driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def move_top(self):
        sleep(3)
        action = TouchAction(self._driver)
        rect = self._driver.get_window_rect()
        width, height = rect["width"], rect["height"]
        action.press(x=width * 0.5, y=height * 0.8).wait(200).move_to(x=width * 0.5, y=height * 0.2).release().perform()

    def is_visibility(self, locator):
        return WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(locator))

    def text(self, locator, value=None):
        if value is not None:
            self.find(locator).send_keys(value)
        else:
            return self.find(locator).text
