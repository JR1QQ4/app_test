#!/usr/bin/python
# -*- coding:utf-8 -*-
import csv
import os
import time


class Controller:
    """获取手机电量"""

    def __init__(self, count=1):
        self.counter = count
        self.all_data = [("时间节点", "电量值")]

    def test_process(self):
        """单次测试过程"""
        # 执行获取电量的命令
        result = os.popen("adb shell dumpsys battery")
        power = 0
        # 获取电量的level
        for line in result:
            if "level" in line:
                power = line.split(":")[1]
        current_time = self.get_current_time()
        # 将获取到的数据存到数组中
        self.all_data.append((current_time, power))

    def run(self):
        """多次执行测试过程"""
        # 设置手机进入非充电状态
        os.popen("adb shell dumpsys battery set status 1")
        while self.counter > 0:
            self.test_process()
            self.counter -= 1
            # 每5秒采集一次数据
            time.sleep(5)

    def get_current_time(self):
        """获取当前的时间戳"""
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def save_data_to_csv(self):
        """数据的存储"""
        with open("power.csv", "wb") as fs:
            writer = csv.writer(fs)
            writer.writerows(self.all_data)


if __name__ == '__main__':
    controller = Controller(5)
    controller.run()
    controller.save_data_to_csv()
