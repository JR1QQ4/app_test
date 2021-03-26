#!/usr/bin/python
# -*- coding:utf-8 -*-
import yaml
from appium import webdriver

from demo_a.pages.base_page import BasePage
from demo_a.pages.main import Main
from demo_a.utils.get_path import *
from demo_a.utils.get_data import *


class App(BasePage):
    _appPackage = ""
    _appActivity = ""

    def init(self):
        if self._driver is None:
            caps = dict()
            caps["platformName"] = "Android"
            caps["deviceName"] = "Android Emulator"
            caps["noReset"] = True
            caps["appPackage"] = self._appPackage
            caps["appActivity"] = self._appActivity

            configuration = get_yaml_data(pages_dir + "/configuration.yaml")
            caps["udid"] = configuration["caps"]["uuid"]

            self._driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', caps)
        else:
            self._driver.start_activity(self._appPackage, self._appActivity)
        self._driver.implicitly_wait(5)
        return self

    def main(self):
        return Main(self._driver)
