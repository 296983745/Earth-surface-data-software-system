#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：pythonProject -> timeTest
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/9/21 14:41
@Desc   ：
=================================================='''

import re
import threading
import time

import pandas as pd
import pymysql
from datetime import datetime
import openpyxl
from openpyxl.workbook import Workbook


def get_mysql_list(database, table_name, columnname):
    #  创建连接，指定数据库的ip地址，账号、密码、端口号、要操作的数据库、字符集
    host, user, pwd = 'localhost', 'root', '123456'
    conn = pymysql.connect(host=host, user=user, passwd=pwd, db=database, port=3306,
                           charset='utf8')  # port必须写int类型,MySQL的默认端口为3306. charset必须写utf8
    # 创建游标
    cursor = conn.cursor()
    # 执行sql语句
    sql = 'select {} from {} ;'.format(columnname, table_name)
    cursor.execute(sql)

    # 获取到sql执行的全部结果
    results = cursor.fetchall()
    table_list = []
    for r in results:
        table_list.append(list(r))  # 由于fetchall方法返回的一个元组，需要每一行为列表形式的数据，将其转换为list类型。

    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接

    return list(table_list)  # 返回一个完整的列表数据


def TimeRela(x, y):
    xbegin = x[0]

    bTimeI = datetime.fromisoformat(x[0][0][:-1]).year
    eTimeI = datetime.fromisoformat(x[1][0][:-1]).year
    bTimeJ = datetime.fromisoformat(y[0][0][:-1]).year
    eTimeJ = datetime.fromisoformat(y[1][0][:-1]).year
    # print(bTimeI)
    # print(eTimeI)
    # print(bTimeJ)
    # print(eTimeJ)
    # bTimeI = x.Begine
    # eTimeI = x.End
    # bTimeJ = y.Begine
    # eTimeJ = y.End
    longI = eTimeI - bTimeI + 1  # I时间跨度
    longJ = eTimeJ - bTimeJ + 1  # J时间长度
    midJ = (bTimeJ + eTimeJ) / 2  # J中间
    midI = (eTimeI + bTimeI) / 2
    D = abs(midI - midJ) + 1  # 中心点距离 #绝对值中心
    rI = longI / 2  # 半径
    rJ = longJ / 2
    timeWeight = float(0)
    timere = "NO"
    timeTopo = float(0)  # 拓扑关系值基准
    timeMet = float(0)
    timeSeq = float(0)

    if (bTimeJ == bTimeI and eTimeJ == eTimeI):
        timeTopo = 1
        timeMet = 1
        timeSeq = 1
        timeWeight = 1
        timere = "Equals"
    elif (bTimeJ < bTimeI and eTimeJ > eTimeI):
        timeTopo = 0.667  # 1在2之间during
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
        timeTopo = 0.5  # 1包含2includes
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
    return str(format(timeWeight, '.3f')) + "-" + timere
    # return timeWeight,timere


def getbyid(name, feature1, feature2, id):
    # 连接到数据库
    db = pymysql.connect(host='localhost', user='root', password='123456', database='earthdata')
    cursor = db.cursor()
    query = 'SELECT {},{},{} FROM nasa3 WHERE id = %s;'.format(name, feature1, feature2)
    cursor.execute(query, id)
    res = cursor.fetchone()
    # 提交更改并关闭连接
    db.commit()
    db.close()
    return res[0], res[1], res[2]


if __name__ == '__main__':
    # 从数据库中取元素
    beginTime = get_mysql_list('earthdata', 'nasa2', 'Beginning_Date_Time')
    endTime = get_mysql_list('earthdata', 'nasa2', 'Ending_Date_Time')
    print(len(beginTime))
    # print(beginTime[0][0])
    # print(endTime[0][0])
    merged_time = [[x, y] for x, y in zip(beginTime, endTime)]
    print(merged_time)
    # print(merged_time[0][0])
    # bTimeI = datetime.fromisoformat(merged_time[0][0][0][:-1]).year
    # eTimeI = datetime.fromisoformat(merged_time[0][1][0][:-1]).year
    # print(bTimeI)
    # print(eTimeI)
    # semtime = []
    # for i in range(10):
    #     line = []
    #     for j in range(10):
    #         simi = TimeRela(merged_time[i], merged_time[j])
    #         # print(simi,merged_time[i],merged_time[j])
    #         line.append(simi)
    #     semtime.append(line)
    # print(semtime)
    #
    # data_df = pd.DataFrame(semtime)
    # # 将文件写入excel表格中
    # writer = pd.ExcelWriter('timesimiEng.xlsx')  # 关键2，创建excel表格
    # data_df.to_excel(writer, 'page_1')  # 关键3，float_format 控制精度，将data_df写到hhh表格的第一页中。若多个文件，可以在page_2中写入
    # writer._save()

    # 创建一个新的Excel文件
    workbook = Workbook()
    sheet = workbook.active
    # 自定义列名

    column_names = ["数据集1", "数据集2", "开始时间1", "结束时间1", "开始时间2", "结束时间2", "时间关联度"]
    # 写入列名
    sheet.append(column_names)
    # 创建一个互斥锁
    lock = threading.Lock()

    for i in range(len(merged_time)):
        for j in range(len(merged_time)):
            simi = TimeRela(merged_time[i], merged_time[j])
            if i != j:
                time.sleep(0.02)
                Entry_Title1, Beginning_Date_Time1, Ending_Date_Time1 = getbyid("Entry_Title", "Beginning_Date_Time",
                                                                                "Ending_Date_Time", i + 1)
                Entry_Title2, Beginning_Date_Time2, Ending_Date_Time2 = getbyid("Entry_Title", "Beginning_Date_Time",
                                                                                "Ending_Date_Time", j + 1)
                # data = [f"{Entry_Title1}", f"{Entry_Title2}", f"{Beginning_Date_Time1}", f"{Ending_Date_Time1}",
                #         f"{Beginning_Date_Time2}", f"{Ending_Date_Time2}", f"{format(simi, '.3f')}"]
                data1=[Entry_Title1, Entry_Title2,Beginning_Date_Time1, Ending_Date_Time1, Beginning_Date_Time2,Ending_Date_Time2,format(simi)]

                sheet.append(data1)
    workbook.save("timeEng.xlsx")
