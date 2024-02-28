#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> test
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/11/11 20:25
@Desc   ：
=================================================='''
import requests

# 替换为您的查询和API密钥
query = "吉林"
api_key = "e657ab2ba98d4801a576c1ba2297e304"

# 发起API请求
url = f"https://api.opencagedata.com/geocode/v1/json?q={query}&key={api_key}"
response = requests.get(url)
data = response.json()

# 解析API响应
results = data["results"]
if results:
    # 提取经纬度坐标
    latitude = results[0]["geometry"]["lat"]
    longitude = results[0]["geometry"]["lng"]

    print("Latitude:", latitude)
    print("Longitude:", longitude)
else:
    print("No results found.")