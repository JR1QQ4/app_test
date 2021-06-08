#!/usr/bin/python
# -*- coding:utf-8 -*-
import csv
import os
import time


class Controller:
    """获取手机电量"""

    def __init__(self, count=1):
        self.counter = count
        self.all_data = [("id", "vss", "rss")]

    def analyze_data(self):
        """分析数据"""
        content = self.readfile()
        i = 0
        for line in content:
            if "$package" in line:
                print(line)
                line = "#".join(line.split())
                vss = line.split("#")[5].strip("k")
                rss = line.split("#")[6].strip("k")
                # 将获取到的数据存到数组中
                self.all_data.append((str(i), vss, rss))
                i += 1

    def readfile(self):
        """读取数据文件"""
        with open('mem_info', 'r') as fs:
            content = fs.readlines()
        return content

    def get_current_time(self):
        """获取当前的时间戳"""
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def save_data_to_csv(self):
        """数据的存储"""
        with open("mem_info.csv", "wb") as fs:
            writer = csv.writer(fs)
            writer.writerows(self.all_data)


if __name__ == '__main__':
    controller = Controller()
    controller.analyze_data()
    controller.save_data_to_csv()
