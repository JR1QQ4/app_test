#!/usr/bin/python
# -*- coding:utf-8 -*-
from demo_b.pages.connect import Connect
from demo_b.pages.main import Main


class TestConnect:
    connect: Connect = None

    def setup_class(self):
        self.connect = Main().init().goto_connect()

    def test_add_connect(self):
        print(self.connect.add_connect())
