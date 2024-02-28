

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> lizi
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/5/15 21:34
@Desc   ：时间关联度计算
=================================================='''
import re

import numpy as np
import pandas as pd

from content.content_yuyi.simi_hownet import get_mysql_list


# 检查下代码
def TimeRela(x, y):
    bTimeI = x.Begin
    eTimeI = x.End
    bTimeJ = y.Begin
    eTimeJ = y.End
    # print(bTimeI)
    # print(eTimeI)
    # print(bTimeJ)
    # print(eTimeJ)
    longI = eTimeI - bTimeI + 1#I时间跨度
    longJ = eTimeJ - bTimeJ + 1 #J时间长度
    midJ = (bTimeJ + eTimeJ) / 2 #J中间
    midI = (eTimeI + bTimeI) / 2
    D = abs(midI - midJ) + 1  # 中心点距离 #绝对值中心
    rI = longI / 2  # 半径
    rJ = longJ / 2
    timeWeight = float(0)
    timere = "NO"
    timeTopo = float(0)#拓扑关系值基准
    timeMet = float(0)
    timeSeq = float(0)

    if (bTimeJ == bTimeI and eTimeJ == eTimeI):
        timeTopo = 1
        timeMet = 1
        timeSeq = 1
        timeWeight = 1
        timere = "Equals"
    elif (bTimeJ < bTimeI and eTimeJ > eTimeI):
        timeTopo = 0.667 #1在2之间during
        timeMet = longI / longJ
        timere = "During"
        if (midI < midJ):
            timeSeq = 2 / 3
        elif (midI == midJ):
            timeSeq = 1 / 2
        else:
            timeSeq = 1 / 3
        timeWeight = timeTopo + 0.333 * (0.738 * timeMet + 0.262 * timeSeq)
    elif (bTimeJ > bTimeI and eTimeJ < eTimeI):
        timeTopo = 0.5   #1包含2includes
        timeMet = longJ / longI
        if (midI < midJ):
            timeSeq = 2 / 3
        elif (midI == midJ):
            timeSeq = 1 / 2
        else:
            timeSeq = 1 / 3
        timere = "Includes"
        timeWeight = timeTopo + 0.167 * (0.738 * timeMet + 0.262 * timeSeq)
    elif (bTimeJ > bTimeI and eTimeJ == eTimeI):
        timeTopo = 0.5
        timeMet = longJ / longI
        timeSeq = 2 / 3
        timere = "EndedBy"
        timeWeight = timeTopo + 0.167 * (0.738 * timeMet + 0.262 * timeSeq)
    elif (bTimeI > bTimeJ and eTimeI == eTimeJ):
        timeTopo = 0.667
        timeMet = longI / longJ
        timeSeq = 1 / 3
        timere = "Ends"
        timeWeight = timeTopo + 0.333 * (0.738 * timeMet + 0.262 * timeSeq)
    elif (bTimeJ == bTimeI and eTimeJ < eTimeI):
        timeTopo = 0.5
        timeMet = longJ / longI
        timeSeq = 1 / 3
        timere = "StartedBy"
        timeWeight = timeTopo + 0.167 * (0.738 * timeMet + 0.262 * timeSeq)
    elif (bTimeJ == bTimeI and eTimeJ > eTimeI):
        timeTopo = 0.667
        timeMet = longI / longJ
        timeSeq = 2 / 3
        timere = "Starts"
        timeWeight = timeTopo + 0.333 * (0.738 * timeMet + 0.262 * timeSeq)
    elif (bTimeJ < eTimeI and bTimeJ > bTimeI and eTimeJ > eTimeI):
        timeTopo = 0.5
        timeMet = (eTimeI - bTimeJ + 1) / longI
        timeSeq = 2 / 3
        timere = "OverlappedBy"
        timeWeight = timeTopo + 0.167 * (0.738 * timeMet + 0.262 * timeSeq)
    elif (bTimeI < eTimeJ and bTimeI > bTimeJ and eTimeI > eTimeJ):
        timeTopo = 0.5
        timeMet = (eTimeJ - bTimeI + 1) / longI
        timeSeq = 1 / 3
        timere = "Overlaps"
        timeWeight = timeTopo + 0.167 * (0.738 * timeMet + 0.262 * timeSeq)
    elif (bTimeJ == eTimeI and eTimeJ > eTimeI):
        timeTopo = 0.333
        timeSeq = 2 / 3
        timere = "MetBy"
        timeWeight = timeTopo + 0.167 * (0.738 * timeMet + 0.262 * timeSeq)
    elif (bTimeI == eTimeJ and eTimeI > eTimeJ):
        timeTopo = 0.333
        timeSeq = 1 / 3
        timere = "Meets"
        timeWeight = timeTopo + 0.167 * (0.738 * timeMet + 0.262 * timeSeq)
    elif (eTimeJ < bTimeI):
        timeTopo = 0
        timeMet = 1 / D
        timeSeq = 1 / 3
        timere = "After"
        timeWeight = timeTopo + 0.333 * (0.738 * timeMet + 0.262 * timeSeq)
    elif (eTimeI < bTimeJ):
        timeTopo = 0
        timeMet = 1 / D
        timeSeq = 2 / 3
        timere = "Before"
        timeWeight = timeTopo + 0.333 * (0.738 * timeMet + 0.262 * timeSeq)
    # return str(format(timeWeight, '.3f')) + "-" + timere
    return timeWeight,timere


# 整理格式
def reformat(x):
    res = []
    for i in x:
        result = re.search('(\d{4}).*?(\d{4}).*', i[0])
        if result != None:
            tmp = MyClass(int(result.group(1)), int(result.group(2)))
        elif result == None:
            result = re.search('(\d{4})', i[0])
            if result != None:
                tmp = MyClass(int(result.group(1)), int(result.group(1)))
            else:
                tmp = MyClass(0, 0)
        res.append(tmp)
    return res


class MyClass:
    def __init__(self, Begin, End):
        self.Begin = Begin
        self.End = End


if __name__ == '__main__':
    # 从数据库中取元素
    x = get_mysql_list('earthdata', 'data_copy', 'DateTime')
    # print(x)
    # 整理格式
    x = reformat(x)
    # print(x[0])
    semtime =[]
    for i in range(len(x)):
        line=[]
        for j in range(len(x)):
            simi = TimeRela(x[i], x[j])
            print(simi,i,j)
            line.append(simi)
        semtime.append(line)
    print(semtime)
    data_df = pd.DataFrame(semtime)
    # 将文件写入excel表格中
    writer = pd.ExcelWriter('timesimi.xlsx')  # 关键2，创建excel表格
    data_df.to_excel(writer, 'page_1')  # 关键3，float_format 控制精度，将data_df写到hhh表格的第一页中。若多个文件，可以在page_2中写入
    writer.save()  # 关键4
