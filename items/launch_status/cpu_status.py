#!/usr/bin/python
# -*- coding:utf-8 -*-
import csv
import os
import time


class Controller:
    """获取 CPU 占用情况"""

    def __init__(self, count=1):
        self.counter = count
        self.all_data = [("时间节点", "CPU占用率")]

    def test_process(self):
        """单次测试过程"""
        result = os.popen("adb shell dumpsys cpuinfo | grep app_package")
        cpu_value = None
        for line in result.readlines():
            cpu_value = line.split("%")[0]
        current_time = self.get_current_time()
        self.all_data.append((current_time, cpu_value))

    def run(self):
        """多次执行测试过程"""
        while self.counter > 0:
            self.test_process()
            self.counter -= 1
            # 每隔多长时间进行统计
            time.sleep(5)

    def get_current_time(self):
        """获取当前的时间戳"""
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def save_data_to_csv(self):
        """数据的存储"""
        with open("cpu_status.csv", "wb") as fs:
            writer = csv.writer(fs)
            writer.writerows(self.all_data)


if __name__ == '__main__':
    controller = Controller(10)
    controller.run()
    controller.save_data_to_csv()
