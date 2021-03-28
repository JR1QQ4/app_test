#!/usr/bin/python
# -*- coding:utf-8 -*-
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from api_test.main import Main


class TestAPI:
    main = None

    def setup_class(self):
        self.main = Main()

    def test_search(self):
        self.main.search()

    def test_search_and_get_price(self):
        print(self.main.search_and_get_price())

    def test_search_and_show_attribute(self):
        self.main.search_and_show_attribute()

    def test_move_to(self):
        cur = {"x": 732, "y": 2048}
        pos = {"x": 732, "y": 484}
        # self.main.move_to(cur, pos)
        self.main.move_to(cur, pos)

    def test_scroll_and_search_with_android_selector(self):
        self.main.scroll_and_search_with_android_selector()

    def test_toast(self):
        self.main.toast()
