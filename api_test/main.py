#!/usr/bin/python
# -*- coding:utf-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.gsm import GsmCallActions
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
    _search_result_first = (MobileBy.ID, 'com.xueqiu.android:id/name')
    _result_item = (MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/ll_stock_result_view"]'
                                    '//*[@text="$value"]/../..')
    _result_item_code = (MobileBy.XPATH, '//*[@text="$code"]')
    _result_price = (MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/ll_stock_result_view"]'
                                     '//*[@text="$value"]/../..//*[@resource-id="com.xueqiu.android:id/current_price"]')
    _result_price_with_code = (MobileBy.XPATH, '//*[@text="$code"]/../../..'
                                               '//*[@resource-id="com.xueqiu.android:id/current_price"]')
    # 取消搜索
    _close_search = (MobileBy.ID, 'com.xueqiu.android:id/action_close')
    # tab导航
    _tab = (MobileBy.XPATH, '//*[@resource-id="android:id/tabs"]//*[@text="$tab"]/..')

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
                        # "avd": "Pixel_23_6",  # 启动模拟器
                        "dontStopAppOnRest": True,  # 首次启动 app 时不停止 app（可以调试或者运行的时候提升运行速度）
                        "skipDeviceInitialization": True,  # 跳过安装，权限设置等操作（可以调试或者运行的时候提升运行速度）
                        # "newCommandTimeout": 300,  # 每一条命令执行的间隔时间
                        # "uuid": "",  # 用于
                        # "autoGrantPermissions": True,  # 用于权限管理，设置了这个，就不需要设置 noRest
                        "chromedriverExecutable": "C:\\webdriver\\chromedriver.exe"  # 用于测试 webview 页面
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

    def clear(self, locator):
        self.find(locator).clear()

    def search_get_price(self, value, code):
        self.click(self._search_input)
        self.text(self._search_text, value)
        self.click(self._search_result_first)
        price = self.text((self._result_price_with_code[0], self._result_price_with_code[1].replace("$code", code)))
        self.click(self._close_search)
        return price

    def mobile_call(self, phone_number="13883256868", action=GsmCallActions.CALL):
        """mumu 模拟器不支持，需要使用原生的"""
        # action:
        # GsmCallActions.CALL
        # GsmCallActions.ACCEPT
        # GsmCallActions.CANCEL
        # GsmCallActions.HOLD
        self._driver.make_gsm_call(phone_number, action)

    def msg(self, phone_number="13537773695", message="Hello world!"):
        """mumu 模拟器不支持，需要使用原生的"""
        self._driver.send_sms(phone_number, message)

    def network(self, connection_type=1):

        self._driver.set_network_connection(connection_type)
        sleep(3)
        self._driver.set_network_connection(6)
        sleep(3)

    def screenshot_as_file(self, path="./photos/img.png"):
        self._driver.get_screenshot_as_file(path)

    def webview(self):
        self.click((self._tab[0], self._tab[1].replace("$tab", "交易")))
        sleep(10)
        print(self._driver.contexts)

        # 立即开户，切换到 webview
        self._driver.switch_to.context(self._driver.contexts[-1])
        sleep(10)
        # print(self._driver.window_handles)
        loc1 = (MobileBy.XPATH, "//*[id='Layout_app_3V4']/div/div/ul/li[1]/div[2]/h1")
        WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(loc1))
        self.click(loc1)
        sleep(10)
        handle = self._driver.window_handles[-1]
        self._driver.switch_to.window(handle)

        # 开户信息填写
        loc2 = (MobileBy.ID, "phone-number")
        loc3 = (MobileBy.ID, "code")
        loc4 = (MobileBy.CSS_SELECTOR, ".btn-submit")
        self.text(loc2, "13810120202")
        self.text(loc3, "6666")
        self.click(loc4)
