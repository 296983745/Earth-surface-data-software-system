# import xml.dom.minidom
import os
#
#
# flie = 'D:\\01study\\01python_item\pratice\Repetition\Topic\C179001815-SEDAC.dif10'  # 写文件目录包括文件名
# # 问题1格式化xml文件 直接用os打开打印再写回去就行
# with open(flie, encoding='utf-8') as file_obj:  # 读xml文件
#     xml_str = file_obj.read()
#
# # 格式转换
# xml = xml.dom.minidom.parseString(xml_str.rstrip())
# xml_pretty_str = xml.toprettyxml()
#
# with open(flie, "w", encoding='utf-8') as file_writer:  # utf-8编码写入原文件
#     file_writer.write("%s" % xml_pretty_str)
import os
# import xml.dom.minidom
from xml.dom import minidom
folder_path = 'E:/data2(1)/data/'  # 文件夹路径
file_extension = '.dif10'  # 文件扩展名

# 遍历文件夹下所有文件
for filename in os.listdir(folder_path):
    if filename.endswith(file_extension):
        file_path = os.path.join(folder_path, filename)

        # 读取XML文件
        with open(file_path, encoding='utf-8') as file_obj:
            xml_str = file_obj.read()

        # 解析XML并美化
        xml = minidom.parseString(xml_str.rstrip())
        xml_pretty_str = xml.toprettyxml()
        print(file_path)
        # 将美化后的XML写回文件
        with open(file_path, "w", encoding='utf-8') as file_writer:
            file_writer.write(xml_pretty_str)