#!/usr/bin/python
# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException

from demo_b.pages.base_page import BasePage


class Connect(BasePage):
    _add_connect = (MobileBy.XPATH, '//*[@text="添加成员"]')
    _add_connect_width_ipb = (MobileBy.XPATH, '//*[@text="手动输入添加"]')
    _add_connect_width_all = (MobileBy.XPATH, '//*[@text="完整输入"]')

    _username = (MobileBy.XPATH, '//*[@text="姓名　"]/../*[@class="android.widget.EditText"]')
    _sex = (MobileBy.XPATH, '//*[@text="性别"]/..//*[contains(@class, "TextView") and @text="男"]')
    _sex_choice = (MobileBy.XPATH, '//*[@text="男"]')
    _phone = (MobileBy.XPATH, '//*[@text="手机　"]/..//*[contains(@class, "EditText")]')
    _save = (MobileBy.XPATH, '//*[@text="保存"]')
    _success = (MobileBy.XPATH, '//*[text="添加成功"]')
    _toast = (MobileBy.XPATH, '//*[@class="android.widget.Toast"]')

    def add_connect(self):
        self.move_top()
        self.click(self._add_connect)
        self.click(self._add_connect_width_ipb)
        # try:
        #     ele = self.is_visibility(self._add_connect_width_all)
        #     if ele:
        #         ele.click()
        # except TimeoutException:
        #     pass
        self.text(self._username, "aaaaaaaaa")
        self.click(self._sex)
        self.click(self._sex_choice)
        self.text(self._phone, "13823125462")
        self.click(self._save)
        return self.find_presence(self._toast).text
