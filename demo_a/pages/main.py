#!/usr/bin/python
# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from demo_a.pages.base_page import BasePage


class Main(BasePage):
    def goto_search(self):
        # self.find(MobileBy.ID, 'search').click()
        self.steps("../pages/main.yaml")