#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> csvtotree
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/12/5 16:19
@Desc   ：
=================================================='''
import csv

# 创建空的树形结构
import pandas as pd

# 从Excel文件读取数据
df = pd.read_excel("subclassof.xlsx")

# 创建空的树形结构
tree = {}

# 遍历Excel数据的每一行
for index, row in df.iterrows():
    child = row[0]  # 子节点
    parent = row[2]  # 父节点

    if parent not in tree:
        tree[parent] = []  # 创建父节点

    tree[parent].append(child)  # 将子节点添加到父节点下
print(tree)