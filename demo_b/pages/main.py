#!/usr/bin/python
# -*- coding:utf-8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from demo_b.pages.base_page import BasePage
from demo_b.pages.connect import Connect


class Main(BasePage):
    _app_package = "com.tencent.wework"
    _app_activity = ".launch.WwMainActivity"

    # 定位
    _connect = (MobileBy.XPATH, '//*[@text="通讯录"]')

    def __init(self):
        if self._driver is None:
            caps = dict()
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["platformVersion"] = "6.0.1"
            caps["noReset"] = "true"
            caps["automationName"] = "UiAutomator2"
            caps["appPackage"] = self._app_package
            caps["appActivity"] = self._app_activity
            caps["autoGrantPermissions"] = "true"
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        else:
            self._driver.start_activity(self._app_package, self._app_activity)
        self._driver.implicitly_wait(5)
        return self

    def init(self):
        return self.__init()

    def goto_connect(self):
        self.click(self._connect)
        return Connect(self._driver)

