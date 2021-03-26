#!/usr/bin/python
# -*- coding:utf-8 -*-
from demo_a.pages.app import App


class TestBase:
    app = None

    def setup(self):
        self.app = App()
