#!/usr/bin/python
# -*- coding:utf-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Main:
    _driver: WebDriver
    _appPackage = "com.xueqiu.android"
    _appActivity = ".view.WelcomeActivityAlias"
    # _appActivity = ".common.MainActivity"

    # 搜索框
    _search_input = (MobileBy.ID, "com.xueqiu.android:id/tv_search")
    _search_text = (MobileBy.ID, "com.xueqiu.android:id/search_input_text")
    # 搜索到的内容
    _search_result = (MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/name" and @text="$value"]')
    _result_item = (MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/ll_stock_result_view"]'
                                    '//*[@text="$value"]/../..')
    _result_price = (MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/ll_stock_result_view"]'
                                     '//*[@text="$value"]/../..//*[@resource-id="com.xueqiu.android:id/current_price"]')

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            opts = ["http://127.0.0.1:4723/wd/hub",
                    {
                        "platformName": "Android",
                        "platformVersion": "6.0",
                        "deviceName": "127.0.0.1:7555",
                        "automationName": "UiAutomator2",
                        "appPackage": self._appPackage,  # adb shell dumpsys activity top
                        "appActivity": self._appActivity,
                        "noRest": True,
                        "unicodeKeyBoard": True,
                        "resetKeyBoard": True,
                        "dontStopAppOnRest": True,  # 首次启动 app 时不停止 app（可以调试或者运行的时候提升运行速度）
                        "skipDeviceInitialization": True  # 跳过安装，权限设置等操作（可以调试或者运行的时候提升运行速度）
                    }
                    ]
            self._driver = webdriver.Remote(*opts)
        else:
            self._driver.start_activity(self._appPackage, self._appActivity)
        self._driver.implicitly_wait(10)

    def find(self, locator):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(locator))
        return self._driver.find_element(*locator)

    def click(self, locator):
        ele = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(locator))
        ele.click()

    def text(self, locator, value=""):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(locator))
        if value != "":
            self._driver.find_element(*locator).send_keys(value)
        else:
            return self._driver.find_element(*locator).text

    def search(self, value="阿里巴巴"):
        self.click(self._search_input)
        self.text(self._search_text, value)

    def search_and_get_price(self, value="阿里巴巴"):
        self.click(self._search_input)
        self.text(self._search_text, value)
        self.click((self._search_result[0], self._search_result[1].replace("$value", "阿里巴巴")))
        return float(self.text((self._result_price[0], self._result_price[1].replace("$value", "阿里巴巴"))))

    def search_and_show_attribute(self):
        ele = self.find(self._search_input)
        search_enabled = ele.is_enabled()
        print(ele.text)  # 搜索股票/组合/用户/讨论
        print(ele.location)  # {'x': 219, 'y': 60}
        print(ele.size)  # {'height': 36, 'width': 281}
        if search_enabled:
            ele.click()
            self.text(self._search_text, "alibaba")
            ali_ele = self.find((self._search_result[0], self._search_result[1].replace("$value", "阿里巴巴")))
            # ali_ele.is_displayed()
            print(ali_ele.get_attribute("displayed"))  # true

    def move_to(self, cur=None, target=None):
        sleep(3)
        action = TouchAction(self._driver)
        # action.press(x=cur["x"], y=cur["y"]).wait(200).move_to(x=target["x"], y=target["y"]).release().perform()
        print(self._driver.get_window_rect())
        action.press(x=360, y=1000).wait(200).move_to(x=360, y=280).release().perform()

    def scroll_and_search_with_android_selector(self):
        loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("关注")')
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(loc))
        self._driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        self._driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                         'scrollable(true).instance(0)).'
                                                         'scrollIntoView(new UiSelector().text("玉山落雨").'
                                                         'instance(0));').click()
        sleep(5)

    def toast(self):
        print(self._driver.page_source)