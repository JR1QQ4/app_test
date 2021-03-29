#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from hamcrest import *

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

    @pytest.mark.parametrize("value, code, expect_price", [
        ("alibaba", "BABA", 230),
        ("xiaomi", "01810", 25)
    ])
    def test_search_get_price(self, value, code, expect_price):
        current_price = float(self.main.search_get_price(value, code))
        print(current_price)
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))

    def test_mobile_call(self):
        self.main.mobile_call()

    def test_msg(self):
        self.main.msg()

    def test_network(self):
        self.main.network()

    def test_screenshot_as_file(self):
        self.main.screenshot_as_file()

    def test_webview(self):
        self.main.webview()
