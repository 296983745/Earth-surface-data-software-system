#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> themeFileRead
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/7/31 19:55
@Desc   ：
=================================================='''
# E:\data2(1)\data\C179001815-SEDAC.dif10
import xml.etree.ElementTree as ET
import pymysql
import os

# 连接到数据库
db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="earthdata")
cursor = db.cursor()

folder_path = 'E:\data2(1)\data'
xml_files = [f for f in os.listdir(folder_path) if f.endswith('.dif10')]

for xml_file in xml_files:
    xml_path = os.path.join(folder_path, xml_file)

    # 解析XML文件
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # 命名空间映射
    namespace = {'dif': 'http://gcmd.gsfc.nasa.gov/Aboutus/xml/dif/'}

    # 获取所有的Science_Keywords元素
    science_keywords_elements = root.findall('dif:Science_Keywords', namespace)

    entry_title_element = root.find('dif:Entry_Title', namespace)

    # 获取Entry_Title的文本内容
    entry_title = entry_title_element.text

    # 用于存储关键字的集合
    category_set = set()
    topic_set = set()
    term_set = set()
    variable_level_1_set = set()

    # 遍历每个Science_Keywords元素
    for science_keywords_element in science_keywords_elements:
        # 获取子元素的文本内容
        category = science_keywords_element.find('dif:Category', namespace).text
        topic = science_keywords_element.find('dif:Topic', namespace).text
        term = science_keywords_element.find('dif:Term', namespace).text
        variable_level_1_element = science_keywords_element.find('dif:Variable_Level_1', namespace)
        if variable_level_1_element is not None:
            variable_level_1 = variable_level_1_element.text
        else:
            variable_level_1 = None

        # 将关键字添加到相应的集合中
        category_set.add(category)
        topic_set.add(topic)
        term_set.add(term)
        if variable_level_1 is not None:
            variable_level_1_set.add(variable_level_1)

    # 数据库连接与操作
    # 插入去重后的关键字
    insert_query = "INSERT INTO nasa (Entry_Title, Category, Topic, Term, Variable_Level_1) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Category = VALUES(Category), Topic = VALUES(Topic), Term = VALUES(Term), Variable_Level_1 = VALUES(Variable_Level_1)"

    # 检查数据长度并截断超过长度限制的字符串
    entry_title = entry_title[:255]  # Entry_Title 列长度限制为 255
    category_data = ', '.join(category_set)[:500]  # Category 列长度限制为 500
    topic_data = ', '.join(topic_set)[:500]  # Topic 列长度限制为 500
    term_data = ', '.join(term_set)[:500]  # Term 列长度限制为 500
    variable_level_1_data = ', '.join(variable_level_1_set)[:500]  # Variable_Level_1 列长度限制为 500

    data = (entry_title, category_data, topic_data, term_data, variable_level_1_data)
    cursor.execute(insert_query, data)
    # 提交更改
    db.commit()

# 关闭数据库连接
db.close()