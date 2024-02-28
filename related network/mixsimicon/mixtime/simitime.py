#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> test
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/11/11 10:20
@Desc   ：
=================================================='''
from datetime import datetime

import openpyxl

from Time.TimeSimi import reformat, TimeRela
from content.content_yuyi.simi_yuxian import get_mysql_list


class MyClass:
    def __init__(self, Begine, End):
        self.Begine = Begine
        self.End = End


if __name__ == '__main__':
    name1 = get_mysql_list('earthdata', 'nasa1110', 'Entry_Title')
    name2 = get_mysql_list('earthdata', 'datatopic', 'DataName')
    # 合并两个列表
    combined_list = name2 + name1  # 中加英
    print(len(combined_list))
    beginTime = get_mysql_list('earthdata', 'nasa1110', 'Beginning_Date_Time')
    endTime = get_mysql_list('earthdata', 'nasa1110', 'Ending_Date_Time')
    # print(beginTime[0][0])
    # print(endTime[0][0])
    merged_time = [[x, y] for x, y in zip(beginTime, endTime)]
    #merged_time是英文
    x = get_mysql_list('earthdata', 'datatopic', 'DateTime')
    # print(x)
    # 整理格式
    x = reformat(x)

    for i in range(len(merged_time)):
        tmp=MyClass(int(datetime.fromisoformat(merged_time[i][0][0][:-1]).year),int(datetime.fromisoformat(merged_time[i][1][0][:-1]).year))
        x.append(tmp)
    print(len(x))

    excel_name = "mixsimitim3.xlsx"
    wb = openpyxl.load_workbook(excel_name)
    ws = wb.active

    # 获取当前选中的工作表

    sheet = wb.active
    column_names = ["name1", "name2", "开始时间", "结束时间", "内容关联度"]

    excel_name2 = "mixsimitim4.xlsx"
    wb2 = openpyxl.load_workbook(excel_name2)
    ws2 = wb2.active

    # 获取当前选中的工作表

    sheet2 = wb2.active
    column_names2 = ["name1", "name2", "开始时间", "结束时间", "内容关联度"]
    # 写入列名
    sheet2.append(column_names2)
    sheet.append(column_names)
    for i in range(len(x)):
        for j in range(len(x)):
            if i!=j:
                simitim,topu=TimeRela(x[i],x[j])
                print(simitim)
                simi=str(format(simitim, '.3f')) + "-" + topu
                if(simitim>0.8):
                    data = [combined_list[i][0], combined_list[j][0], str(x[i].Begine) + " " + str(x[i].End),str(x[j].Begine) + " " + str(x[j].End), simi]
                    sheet2.append(data)
                data1 = [combined_list[i][0], combined_list[j][0], str(x[i].Begine) + " " + str(x[i].End),str(x[j].Begine) + " " + str(x[j].End), simi]
                sheet.append(data1)

    wb.save(excel_name)
    print('finish')
    wb2.save(excel_name2)
    print('finish')




