#!/usr/bin/python
# -*- coding:utf-8 -*-

search_result = ('', '//*[@resource-id="com.xueqiu.android:id/name" and @text="$value"]')
search_result = (search_result[0], search_result[1].replace("$value", "阿里巴巴"))
print(search_result)
