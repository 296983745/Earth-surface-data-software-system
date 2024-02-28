#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> mintopictestchn
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/12/1 9:33
@Desc   ：
=================================================='''
import pandas as pd
from text2vec import Similarity

from content.content_yuyi.simi_hownet import get_mysql_list

if __name__ == '__main__':
    topic= get_mysql_list('earthdata', 'datatopic', 'MainOfKind')
    name = get_mysql_list('earthdata', 'datatopic', 'DataName')
    # print(name)
    # for i in range(len(topic)):、
    sim_model = Similarity("D:\\01study\\paraphrase-multilingual-MiniLM-L12-v2")
    new_data=[]
    for i in range(len(topic)):
        for j in range(i,len(topic)):
            simi=sim_model.get_scores(topic[i][0],topic[j][0])
            if len(simi)>0:
                simi=simi[0][0]
                new_row = {
                    'name1': name[i][0],
                    'name2': name[j][0],
                    'topic1': topic[i][0],
                    'topic2': topic[j][0],
                    'simi': simi
                }
                new_data.append(new_row)


    df = pd.read_csv('owlfacechn.csv')

    # 创建新的 DataFrame
    new_rows = pd.DataFrame(new_data)

    # 将新数据插入到 DataFrame 的末尾
    df = pd.concat([df, new_rows], ignore_index=True)

    # 将数据保存到 CSV 文件
    df.to_csv('owlfacechn.csv', index=False)
    print('finish')