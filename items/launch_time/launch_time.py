#!/usr/bin/python
# -*- coding:utf-8 -*-
import csv
import os
import time


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
        # 冷启动
        # shell = 'adb shell am force-stop package'
        # 热启动
        shell = 'adb shell input keyevent 3'
        os.popen(cmd=shell)

    def get_launch_time(self):
        """获取启动时间"""
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.start_time = line.split(":")[1]
                break
        return self.start_time


class Controller:
    """获取启动时间情况"""
    def __init__(self, count=1):
        self.app = App()
        self.counter = count
        self.all_data = [("时间节点", "耗时")]

    def test_process(self):
        """单次测试过程"""
        self.app.launch_app()
        time.sleep(5)
        elapsed_time = self.app.get_launch_time()
        self.app.stop_app()
        time.sleep(3)
        current_time = self.get_current_time()
        self.all_data.append((current_time, elapsed_time))

    def run(self):
        while self.counter > 0:
            self.test_process()
            self.counter -= 1

    def get_current_time(self):
        """获取当前的时间戳"""
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def save_data_to_csv(self):
        """数据的存储"""
        with open("start_time.csv", "wb") as fs:
            writer = csv.writer(fs)
            writer.writerows(self.all_data)


if __name__ == '__main__':
    controller = Controller(10)
    controller.run()
    controller.save_data_to_csv()
