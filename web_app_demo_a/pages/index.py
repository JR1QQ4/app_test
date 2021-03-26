#!/usr/bin/python
# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from web_app_demo_a.pages.base_page import BasePage


class Index(BasePage):
    _url = "https://m.baidu.com"
    _search_input = (MobileBy.CSS_SELECTOR, "input#index-kw")
    _search_click = (MobileBy.CSS_SELECTOR, "button#index-bn")

    def search(self, w):
        self.send_keys(self._search_input, w)
        self.click(self._search_click)
        return self.get_title()
