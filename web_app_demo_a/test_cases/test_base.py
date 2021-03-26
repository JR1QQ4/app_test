#!/usr/bin/python
# -*- coding:utf-8 -*-
from web_app_demo_a.pages.index import Index


class TestBase:
    index = None

    def setup_class(self):
        self.index = Index()

    # def teardown_class(self):
    #     self.index.quit()
