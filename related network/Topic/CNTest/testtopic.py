#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> testtopic
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/10/18 21:48
@Desc   ：
=================================================='''
import threading

import openpyxl
from openpyxl.packaging import workbook


from content.content_yuyi.simi_yuxian import get_mysql_list

if __name__ == '__main__':
    topic= get_mysql_list('earthdata', 'datatopic', 'MainOfKind')
    name = get_mysql_list('earthdata', 'datatopic', 'DataName')
    # for i in range(len(topic)):
    #     print(topic[i])
    # print(name)
    # nametopic = list(zip(name, topic))
    # print(nametopic)


results = []  # 存储处理后的结果
#
# 处理每个 data_list
for data_list in topic:
    subresults = []  # 存储每个 data_list 的结果

    for data_str in data_list:
        parts = data_str.split(':')
        subparts = []  # 存储每个部分的元组

        for part in parts:
            subpart = tuple(part.split('\\'))
            subparts.append(subpart)
    results.append(subparts)
for i in range(len(results)):
    print(results[i])
# # 遍历结果并进行比较
excel_name ="topicCHN.xlsx"
wb = openpyxl.load_workbook(excel_name)
ws = wb.active


# 获取当前选中的工作表

sheet = wb.active
column_names = ["name1", "name2", "主题词", "主题词", "主题关联度"]
# 写入列名
sheet.append(column_names)

simss = []
for i in range(len(results)):
    for j in range(i+1,len(results)):
        name1=name[i];
        name2=name[j];
        # print(results[i])
        # print(results[j])
        simsss=[]
        for k in range(len(results[i])):
            simss = []
            for l in range(len(results[j])):
                # print(results[i][k])
                sims = 0
                # print(results[j][l])
                # print(results[i][k][0])
                #                 # print(results[j][l][0])
                #                 # print(results[i][k][1])
                # print(results[j][l][1])
                if results[i][k][0]==results[j][l][0]:
                    sims+=0.5;
                    if results[i][k][1]==results[j][l][1]:
                        sims+=0.5;
                else:
                    sims=0;
                simss.append(sims)
            max_value1 = max(simss)
            simsss.append(max_value1)
        simitopic=max(simsss)
        string_datai = ', '.join([str(item) for item in results[i]])
        string_dataj = ', '.join([str(item) for item in results[j]])
        data1 = [name1[0], name2[0],string_datai, string_dataj , simitopic]
        sheet.append(data1)

wb.save(excel_name)
print('finish')
