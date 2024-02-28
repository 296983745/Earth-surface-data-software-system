#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> GTRD1220
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/12/20 9:35
@Desc   ：
=================================================='''
import pandas as pd
from scipy.stats import stats

from Topic.mixtopic.test1205 import simimix
from mixsimicon.mixcon.test import sim_model

# 读取 Excel 表格
df = pd.read_excel("E:\\02-地表研发项目\\001-会议纪要&前期录像方案\\23.12.23会议重点研发\\GTRD\\Geo-Terminology_Relatedness_Dataset_means.xlsx")

# 逐行读取 TERM_A 列和 TERM_B 列
GTRD=[]
test=[]
for index, row in df.iterrows():
    term_a = row['TERM_A']
    term_b = row['TREM_B']
    RELATEDNESS_1=row['RELATEDNESS']
    GTRD.append(RELATEDNESS_1)
    simi=simimix(term_a,term_b)
    # simi=sim_model.get_scores(term_a,term_b)
    test.append(simi[0][0])
print(GTRD)
print(test)
res=stats.spearmanr(GTRD,test)

print(res)
# 将test列表添加到DataFrame中
# df['New_Column'] = test

# 将DataFrame保存回Excel文件
df.to_excel("E:\\02-地表研发项目\\001-会议纪要&前期录像方案\\23.12.23会议重点研发\\GTRD\\Geo-Terminology_Relatedness_Dataset_means.xlsx", index=False)





