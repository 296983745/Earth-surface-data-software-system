import json
import os
import xml
from xml.etree import ElementTree as ET
from lxml import etree
"""
实现从xml文件中读取数据
"""
# 全局唯一标识
unique_id = 1


# 遍历所有的节点
def walkData(root_node, level, result_list):
    global unique_id
    children_node = list(root_node)
    if len(children_node) == 0: # 叶子节点
        result_dict={"unique_id":unique_id,"level":level,"tag":etree.QName(root_node.tag).localname,"text":root_node.text}
        result_list.append(result_dict)
        unique_id += 1
        return
    else:
        result_dict = {"unique_id": unique_id, "level": level, "tag": etree.QName(root_node.tag).localname,
                       "text": root_node.text}
        result_list.append(result_dict)
        unique_id += 1
    for child in children_node:
        walkData(child, level + 1, result_list)
    return


def getXmlData(file_name):
    level = 1  # 节点的深度从1开始
    result_list = []
    root = ET.parse(file_name).getroot()
    walkData(root, level, result_list)
    return result_list


if __name__ == '__main__':
    'd:\\fenlei2.xml'
    file_name = 'E:\data2(1)\data\C179001815-SEDAC.dif10'
    R = getXmlData(file_name)
    dict_name1 = {}
    for x in R:
        while(dict_name1.get(x["tag"])):
            x["tag"]=x["tag"]+"1"
        dict_name1.update({x["tag"]: x["text"]})
        # print(x)
        pass
        # f.write(json.dumps(dict_name1))
    print(dict_name1)


