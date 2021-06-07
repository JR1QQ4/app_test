#!/usr/bin/python
# -*- coding:utf-8 -*-
import csv
import os
import time


class Controller:
    """获取流量使用情况"""

    def __init__(self, count=1):
        self.counter = count
        self.all_data = [("时间节点", "最终流量值")]

    def my_atoi(self, s: str):
        """atoi (表示 ascii to integer)是把字符串转换成整型数的一个函数"""
        import re
        pattern = r"[\s]*[+-]?[\d]+"
        match = re.match(pattern, s)
        if match:
            res = int(match.group(0))
            if res > 2 ** 31 - 1:
                res = 2 ** 31 - 1
            if res < - 2 ** 31:
                res = - 2 ** 31
        else:
            res = 0
        return res

    def test_process(self):
        """单次测试过程"""
        # 获取PID
        result = os.popen("adb shell ps | grep $package")
        pid = result.readlines()[0].split(" ")[5]
        # 获取对应PID的流量值
        traffic = os.popen('adb shell cat /proc/' + pid + '/net/dev')
        receive = transmit = receive2 = transmit2 = ""
        for line in traffic:
            if "eth0" in line:  # 网卡1
                line = "#".join(line.split())
                # 获取收到和发出的流量
                receive = line.split("#")[1]
                transmit = line.split("#")[9]
            elif "eth1" in line:  # 网卡2
                line = "#".join(line.split())
                receive2 = line.split("#")[1]
                transmit2 = line.split("#")[9]
        # 计算所有流量之和
        all_traffic = self.my_atoi(receive) + self.my_atoi(transmit) + self.my_atoi(receive2) + self.my_atoi(transmit2)
        # 按KB计算流量值
        all_traffic = all_traffic / 1024
        current_time = self.get_current_time()
        self.all_data.append((current_time, all_traffic))

    def run(self):
        """多次执行测试过程"""
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
        with open("traffic.csv", "wb") as fs:
            writer = csv.writer(fs)
            writer.writerows(self.all_data)


if __name__ == '__main__':
    controller = Controller(3)
    controller.run()
    controller.save_data_to_csv()
