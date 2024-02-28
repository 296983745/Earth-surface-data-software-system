#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> test
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/9/22 8:55
@Desc   ：
=================================================='''
import pymysql


def getbyid1(name, feature1, feature2,feature3, id):
    # 连接到数据库
    db = pymysql.connect(host='localhost', user='root', password='123456', database='earthdata')
    cursor = db.cursor()
    query = 'SELECT {},{},{},{} FROM nasa3 WHERE id = %s;'.format(name, feature1, feature2,feature3)
    cursor.execute(query, id)
    res = cursor.fetchone()
    # 提交更改并关闭连接
    db.commit()
    db.close()
    return res[0], res[1], res[2], res[3]


Entry_Title1, Topic1, Term1, Variable_Level_11= getbyid1("Entry_Title", "Topic","Term","Variable_Level_1", 1)
print(Entry_Title1)
print(Topic1)
print(Term1)
print(Variable_Level_11)