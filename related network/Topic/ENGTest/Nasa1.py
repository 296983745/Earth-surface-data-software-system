#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> Nasa1
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/10/28 13:14
@Desc   ：
=================================================='''
import difflib
import openpyxl
def compute_similarity(words1, words2):
    # 将两组单词转换为字符串
    str1 = ' '.join(words1)
    str2 = ' '.join(words2)

    # 计算Levenshtein距离
    distance = difflib.SequenceMatcher(None, str1, str2).ratio()

    return distance
from content.content_yuyi.simi_yuxian import get_mysql_list

if __name__ == '__main__':

    entry_Title= get_mysql_list('earthdata', 'engnasa', 'Entry_Title')
    category = get_mysql_list('earthdata', 'engnasa', 'Category')
    topic = get_mysql_list('earthdata', 'engnasa', 'Topic')
    term = get_mysql_list('earthdata', 'engnasa', 'Term')
    variable_Level_1 = get_mysql_list('earthdata', 'nasa1110', 'Variable_Level_1')
    # print(entry_Title)
    # print(category)
    # print(topic)

    excel_name = "topicEng.xlsx"
    wb = openpyxl.load_workbook(excel_name)
    ws = wb.active
    sheet = wb.active
    column_names = ["engname1", "engname2", "主题词", "主题词", "主题关联度"]
    # 写入列名
    sheet.append(column_names)

    for i in range(len(entry_Title)):
        for j in range(len(entry_Title)):
            simi=0;
            if category[i][0]==category[j][0]:
                simi+=0.25;
                topicsimilarity =compute_similarity(topic[i][0],topic[j][0])
                topicsimilarity/=4;
                if topicsimilarity>0.12:
                    simi+=topicsimilarity
                    termsimilarity = compute_similarity(term[i][0], term[j][0])
                    termsimilarity/=4;
                    if termsimilarity>0.12:
                        simi+=termsimilarity
                        variable_Level_1similarity = compute_similarity(variable_Level_1[i][0], variable_Level_1[j][0])
                        variable_Level_1similarity/=4
                        if variable_Level_1similarity>0.12:
                            simi+=variable_Level_1similarity
                else:
                    simi+=topicsimilarity
            else:
                simi=0
            data1 = [entry_Title[i][0], entry_Title[j][0], category[i][0]+"::"+topic[i][0]+"::"+term[i][0]+"::"+variable_Level_1[j][0],category[j][0]+"::"+topic[j][0]+"::"+term[j][0]+"::"+variable_Level_1[j][0] ,simi]
            sheet.append(data1)


    wb.save(excel_name)
    print('finish')



