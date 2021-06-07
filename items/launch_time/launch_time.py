#!/usr/bin/python
# -*- coding:utf-8 -*-
import os


class App:
    def __init__(self):
        self.content = None
        self.start_time = 0

    def launch_app(self):
        """启动 app"""
        shell = 'adb shell am start -W -n package/activity'
        self.content = os.popen(cmd=shell)

    def stop_app(self):
        """停止 app"""
        shell = 'adb shell am force-stop package'
        os.popen(cmd=shell)

    def get_launch_time(self):
        """获取启动时间"""
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.start_time = line.split(":")[1]
                break
        return self.start_time


class Controller:
    def __init__(self, count=1):
        self.app = App()
        self.counter = count

    def test_process(self):
        """单次测试过程"""
        self.app.launch_app()
        self.app.get_launch_time()
        self.app.stop_app()

    def run(self):
        while self.counter > 0:
            self.test_process()
            self.counter -= 1

    def collect_all_data(self):
        pass

    def save_data_to_csv(self):
        pass