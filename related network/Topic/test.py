# #!/usr/bin/env python
# # -*- coding: UTF-8 -*-
# '''=================================================
# @Project -> File   ：Repetition -> test
# @IDE    ：PyCharm
# @Author ：haomengqi
# @Date   ：2023/8/1 11:12
# @Desc   ：
# =================================================='''
# from xml.etree import ElementTree as ET
# from lxml import etree
#
# def walk_data(root_node, level, unique_id):
#     children_node = list(root_node)
#     if len(children_node) == 0:
#         result_dict = {"unique_id": unique_id, "level": level, "tag": root_node.tag, "text": root_node.text}
#         unique_id += 1
#         return [result_dict], unique_id
#     else:
#         result_dict = {"unique_id": unique_id, "level": level, "tag": root_node.tag, "text": root_node.text}
#         unique_id += 1
#     result_list = [result_dict]
#     for child in children_node:
#         child_list, unique_id = walk_data(child, level + 1, unique_id)
#         result_list.extend(child_list)
#     return result_list, unique_id
#
# def get_xml_data(file_name):
#     level = 1
#     unique_id = 1
#     root = ET.parse(file_name).getroot()
#     result_list, _ = walk_data(root, level, unique_id)
#     return result_list
#
# if __name__ == '__main__':
#     file_name = 'E:\data2(1)\data\C179001815-SEDAC.dif10'
#     result_list = get_xml_data(file_name)
#     result_dict = {}
#     for x in result_list:
#         tag = etree.QName(x["tag"]).localname
#         if tag in result_dict:
#             if isinstance(result_dict[tag], list):
#                 result_dict[tag].append(x["text"])
#             else:
#                 result_dict[tag] = [result_dict[tag], x["text"]]
#         else:
#             result_dict[tag] = x["text"]
#     print(result_dict["Entry_Title"])
#     print(result_dict["Category"])
#     print(result_dict["Topic"])
#     print(result_dict["Term"])
#     print(result_dict["Variable_Level_1"])

import os
import pymysql
from xml.etree import ElementTree as ET
from lxml import etree

def walk_data(root_node, level, unique_id):
    children_node = list(root_node)
    if len(children_node) == 0:
        result_dict = {"unique_id": unique_id, "level": level, "tag": root_node.tag, "text": root_node.text}
        unique_id += 1
        return [result_dict], unique_id
    else:
        result_dict = {"unique_id": unique_id, "level": level, "tag": root_node.tag, "text": root_node.text}
        unique_id += 1
    result_list = [result_dict]
    for child in children_node:
        child_list, unique_id = walk_data(child, level + 1, unique_id)
        result_list.extend(child_list)
    return result_list, unique_id

def get_xml_data(file_name):
    level = 1
    unique_id = 1
    root = ET.parse(file_name).getroot()
    result_list, _ = walk_data(root, level, unique_id)
    return result_list

if __name__ == '__main__':
    # 连接MySQL数据库
    db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="earthdata")
    cursor = db.cursor()

    # 指定XML文件夹路径
    folder_path = 'E:\data2(1)\data\\'

    # 遍历文件夹中的每个XML文件
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".dif10"):
            file_path = os.path.join(folder_path, file_name)
            result_list = get_xml_data(file_path)
            result_dict = {}
            for x in result_list:
                tag = etree.QName(x["tag"]).localname
                if tag in ["Entry_Title", "Science_Keywords", "Category", "Topic", "Term", "Variable_Level_1"]:
                    if tag in result_dict:
                        result_dict[tag].append(x["text"])
                    else:
                        result_dict[tag] = [x["text"]]
                else:
                    result_dict[tag] = []

            # 将数据插入到MySQL数据库
            sql = "INSERT INTO nasa (entry_title, science_keywords, category, topic, term, variable_level_1) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (
                result_dict.get("Entry_Title", [""])[0],
                ",".join(result_dict.get("Science_Keywords", [])),
                result_dict.get("Category", [""])[0],
                ",".join(result_dict.get("Topic", [])),
                ",".join(result_dict.get("Term", [])),
                ",".join(result_dict.get("Variable_Level_1", []))
            )
            cursor.execute(sql, values)
            db.commit()

    # 关闭数据库连接
    db.close()