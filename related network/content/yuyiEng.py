#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> yuyiEng
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/9/20 14:55
@Desc   ：1000个英文样本数据
=================================================='''
import threading
import time
from logging import warning

import pandas as pd
import pymysql
from openpyxl.workbook import Workbook
from torch.utils import jit

from content.content_yuyi.simi_yuxian import get_mysql_list, wordsim, semDegree
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：pythonProject -> test2
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/9/20 17:19
@Desc   ：
=================================================='''
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from transformers import logging

# 加载BERT模型和分词器
tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path='D:\\01study\\trans')
model = AutoModel.from_pretrained('D:\\01study\\trans')
# logging.set verbosity warning(


# 定义计算相似度的函数
def calc_similarity(s1, s2):
    # 对句子进行分词，并添加特殊标记
    inputs = tokenizer([s1, s2], return_tensors='pt', padding=True, truncation=True)

    # 将输入传递给BERT模型，并获取输出
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state[:, 0, :].cpu().numpy()

    # 计算余弦相似度，并返回结果
    sim = np.dot(embeddings[0], embeddings[1]) / (np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1]))
    return sim

def wordsimEng(wordlist):
    semword = np.zeros((len(wordlist), len(wordlist)))
    for i in range(len(wordlist)):
        for j in range(len(wordlist)):
            # print(wordlist[i],wordlist[j])
            simi = calc_similarity(wordlist[i], wordlist[j])
            semword[i][j] = format(simi, '.3f')
    return semword



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



if __name__ == '__main__':
    category = get_mysql_list('earthdata', 'nasa3', 'Category')
    topic = get_mysql_list('earthdata', 'nasa3', 'Topic')
    term = get_mysql_list('earthdata', 'nasa3', 'Term')
    variable_Level_1 = get_mysql_list('earthdata', 'nasa3', 'Variable_Level_1')
    # print(term)
    # print(variable_Level_1)
    category = pd.DataFrame(category)
    topic = pd.DataFrame(topic)
    term = pd.DataFrame(term)
    variable_Level_1 = pd.DataFrame(variable_Level_1)
    res = pd.concat([category, topic,term,variable_Level_1], axis=1)
    res.columns = ["category", "topic","term","variable_Level_1"]
    res['word'] = res['category'] + ' ' + res['topic']+ ' ' +res['term'] + ' ' + res['variable_Level_1']
    res.drop('category', axis=1, inplace=True)
    res.drop('topic', axis=1, inplace=True)
    res.drop('term', axis=1, inplace=True)
    res.drop('variable_Level_1', axis=1, inplace=True)
    # 将两列合成一列
    res.word = res.word.replace(r'\s+', ' ', regex=True)
    wordlist = []
    res = res.values.tolist()
    # print(res)
    for row in res:
        row = str(row).replace("/", " ")
        row = str(row).replace(",", " ")
        wordlist.append(row)
    # print(wordlist)
    # print(semDegree("EARTH SCIENCE SOLID EARTH","EARTH SCIENCE AGRICULTURE  HUMAN"))
    # semword = wordsimEng(wordlist)
    # print(semword)
    #
    # # entity_Title = get_mysql_list('earthdata', 'nasa1', 'Entity_Title')
    # # print(entity_Title)
    # data_df = pd.DataFrame(semword)
    # # 将文件写入excel表格中
    # writer = pd.ExcelWriter('contentyuxianEng.xlsx')  # 关键2，创建excel表格
    # data_df.to_excel(writer, 'page_1',
    #                  float_format='%.3f')  # 关键3，float_format 控制精度，将data_df写到hhh表格的第一页中。若多个文件，可以在page_2中写入
    # writer._save()  # 关键4


    workbook = Workbook()
    sheet = workbook.active
    # 自定义列名

    column_names = ["数据集1", "数据集2", "Topic1", "Term1","Variable_Level_11",  "Topic2", "Term2","Variable_Level_12", "内容关联度"]
    # 写入列名
    sheet.append(column_names)
    # 创建一个互斥锁
    lock = threading.Lock()

    for i in range(len(wordlist)):
        for j in range(len(wordlist)):
            simi = calc_similarity(wordlist[i], wordlist[j])
            if i != j:
                time.sleep(0.02)
                Entry_Title1, Topic1, Term1, Variable_Level_11= getbyid1("Entry_Title", "Topic","Term","Variable_Level_1", i + 1)
                Entry_Title2, Topic2, Term2, Variable_Level_12= getbyid1("Entry_Title", "Topic","Term","Variable_Level_1", j + 1)
                # data = [f"{Entry_Title1}", f"{Entry_Title2}", f"{Beginning_Date_Time1}", f"{Ending_Date_Time1}",
                #         f"{Beginning_Date_Time2}", f"{Ending_Date_Time2}", f"{format(simi, '.3f')}"]
                data1 = [Entry_Title1, Entry_Title2, Topic1, Term1, Variable_Level_11,
                         Topic2,Term2,Variable_Level_12, format(simi)]

                sheet.append(data1)
    workbook.save("contentEng.xlsx")