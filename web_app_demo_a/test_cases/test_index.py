#!/usr/bin/python
# -*- coding:utf-8 -*-
from web_app_demo_a.test_cases.test_base import TestBase
from hamcrest import *


class TestIndex(TestBase):
    def test_index_search(self):
        self.index.search("selenium")
        # assert  "selenium - 百度" == self.index.get_title()
        assert_that(self.index.get_title(), equal_to_ignoring_case("selenium - 百度"))

    def test_assert_that(self):
        assert_that(1.23, close_to(1, 0.3))
        my_set = {3, 4, 5}
        assert_that(my_set, contains_inanyorder([1, 2]))
