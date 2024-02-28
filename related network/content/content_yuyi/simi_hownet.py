# 读取内容关键词
import jieba
import pandas as pd
import numpy as np
import jieba.analyse

import OpenHowNet
# -*- coding:utf-8 -*-
# 从MySQL数据库的数据表中读取每一行数据放入列表中，最后返回一个完整的列表
import re
import pymysql
import openpyxl
import pymysql

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


# 计算相似度
def wordsim(wordlist):
    semword = np.zeros((len(wordlist), len(wordlist)))
    for i in range(len(wordlist)):
        k = len(wordlist[i])
        for j in range(len(wordlist)):
            l = len(wordlist[j])
            maxlen = np.array([], dtype=float)
            for p in range(k):
                max1 = 0;
                for q in range(l):
                    simi = semDegree(wordlist[i][p], wordlist[j][q])
                    # sim_b = ws_tool.similarity(wordlist[i][p], wordlist[j][q])
                    max1 = max(simi, max1)
                maxlen = np.append(maxlen, max1)
            semword[i][j] = format(np.mean(maxlen), '.3f')

    return semword


def semDegree(word1, word2):
    return hownet_dict_advanced.calculate_word_similarity(word1, word2)


if __name__ == '__main__':
    x = get_mysql_list('earthdata', 'data_copy', 'MainWord')
    y = get_mysql_list('earthdata', 'data_copy', 'MainOfKind')
    # print(x)
    # print(y)
    df1 = pd.DataFrame(x)
    df2 = pd.DataFrame(y)
    res = pd.concat([df1, df2], axis=1)
    res.columns = ["MainWord", "MainOfKind"]
    res['word'] = res['MainWord'] + res['MainOfKind']
    res.drop('MainWord', axis=1, inplace=True)
    res.drop('MainOfKind', axis=1, inplace=True)
    # 将两列合成一列
    res.word = res.word.replace(r'\s+', ' ', regex=True)
    wordlist = []

    res = res.values.tolist()
    print(res)
    for row in res:
        row = str(row).replace(" ", "")
        row = str(row).replace("/", "")
        wordlist.append(jieba.analyse.extract_tags(row, topK=5))
    print(wordlist)

    OpenHowNet.download()
    hownet_dict_advanced = OpenHowNet.HowNetDict()
    hownet_dict_advanced = OpenHowNet.HowNetDict(init_sim=True)

    # ws_tool = WordSimilarity2010()
    semword = wordsim(res)

    print(semword)
    data_df = pd.DataFrame(semword)
    # 将文件写入excel表格中
    writer = pd.ExcelWriter('contentjieba.xlsx')  # 关键2，创建名称为hhh的excel表格
    data_df.to_excel(writer, 'page_1',
                     float_format='%.3f')  # 关键3，float_format 控制精度，将data_df写到hhh表格的第一页中。若多个文件，可以在page_2中写入
    writer.save()  # 关键4
