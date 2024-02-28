#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> spaceEng
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/9/25 9:05
@Desc   ：
=================================================='''
import time
import pyproj
import pymysql
from openpyxl.workbook import Workbook
from sympy import Polygon
from shapely.geometry import Polygon
from shapely.ops import unary_union
from shapely import affinity
from Time.timeeng.timeTest import get_mysql_list

# 判断空间关联度
def simicoordinate(coords1, coords2):
    if coords1==[(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)] or coords2==[(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)]:
        return 0,'0'
    # 将坐标点转换为 shapely.geometry.Polygon 对象
    poly1 = Polygon(coords1)
    poly2 = Polygon(coords2)
    relation = None
    similarity=0
    # 判断两个地理区域之间的四交模型拓扑关系
    if poly1.equals(poly2):
        similarity = 1.0
        relation = "equals"
    elif poly1.contains(poly2):
        # 计算被包含者占包含者的比例
        ratio = poly2.area / poly1.area
        similarity = ratio * 0.167 + 0.5
        relation = "contains"  # 1包含2 0.5 最多加0.167 包含要边界不相接
    elif poly2.contains(poly1):
        # 交换两个地理区域的顺序，保证第一个地理区域是包含者
        poly1, poly2 = poly2, poly1
        # 计算被包含者占包含者的比例
        ratio = poly2.area / poly1.area
        similarity = ratio * 0.167 + 0.5
        relation = "containsed"  # 被包含
    elif poly1.intersects(poly2):
        # 计算两个地理区域的重叠面积和总面积
        intersection = poly1.intersection(poly2)
        union = unary_union([poly1, poly2])
        # 计算重叠面积占总面积的比例
        overlap_ratio = intersection.area / union.area
        similarity = overlap_ratio * 0.167 + 0.5  # 重叠基础相似度是0.5，根据重叠程度加，最多加0.167
        relation = "overlap"
    elif poly1.disjoint(poly2):
        # 计算两个地理区域的距离
        distance = poly1.distance(poly2)
        # 计算相似度，距离越远，相似度越低
        similarity = 1 / (1 + distance) * 0.333  # 相离 最多0.333
        relation = "disjoint"
    return similarity,relation

def getbyid(name, id):
    # 连接到数据库
    db = pymysql.connect(host='localhost', user='root', password='123456', database='earthdata')
    cursor = db.cursor()
    query = 'SELECT {} FROM nasa3 WHERE id = %s;'.format(name)
    cursor.execute(query, id)
    res = cursor.fetchone()
    # 提交更改并关闭连接
    db.commit()
    db.close()
    return res[0]

if __name__ == '__main__':
    # 从数据库中取元素
    Southernmost_Latitude = get_mysql_list('earthdata', 'nasa3', 'Southernmost_Latitude') # 南边
    Northernmost_Latitude = get_mysql_list('earthdata', 'nasa3', 'Northernmost_Latitude') # 北边
    Westernmost_Longitude = get_mysql_list('earthdata', 'nasa3', 'Westernmost_Longitude') # 西边
    Easternmost_Longitude = get_mysql_list('earthdata', 'nasa3', 'Easternmost_Longitude') # 东边

    zuobiaos=[]
    for i in range(len(Southernmost_Latitude)):
        if Westernmost_Longitude[i][0]=='':
            Westernmost_Longitude[i][0]=0
        if Southernmost_Latitude[i][0] == '':
            Southernmost_Latitude[i][0] = 0
        if Northernmost_Latitude[i][0] == '':
            Northernmost_Latitude[i][0] = 0
        if Easternmost_Longitude[i][0] == '':
            Easternmost_Longitude[i][0] = 0
        Westernmost=float(Westernmost_Longitude[i][0])
        Southernmost=float(Southernmost_Latitude[i][0])
        Northernmost=float(Northernmost_Latitude[i][0])
        Easternmost=float(Easternmost_Longitude[i][0])
        zuobiao = [(Westernmost, Southernmost), (Westernmost, Northernmost), (Easternmost, Northernmost), (Easternmost, Southernmost)]
        zuobiaos.append(zuobiao)
    print(zuobiaos)

    # 创建一个新的Excel文件
    workbook = Workbook()
    sheet = workbook.active
    # merged_time = [[x, y] for x, y in zip(beginTime, endTime)]
    # print(merged_time)
    column_names = ["数据集1", "数据集2", "经纬度范围1", "经纬度范围2", "空间关联度"]
    for i in range(len(zuobiaos)):
        for j in range(len(zuobiaos)):
            simis, simispace = simicoordinate(zuobiaos[i], zuobiaos[j])  # 得到空间相似度和拓扑关系
            print(simispace)
            print(simis)
            if i != j:
                time.sleep(0.03)
                Entry_Title1 = getbyid("Entry_Title", i + 1)
                Entry_Title2 = getbyid("Entry_Title", j + 1)
                data = [f"{Entry_Title1}", f"{Entry_Title2}", f"{zuobiaos[i]}", f"{zuobiaos[j]}", f"{simispace+str(format(simis, '.3f'))}"]
                sheet.append(data)
    workbook.save("spaceEng.xlsx")