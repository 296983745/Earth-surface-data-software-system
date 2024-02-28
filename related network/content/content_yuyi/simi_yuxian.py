
#内容关联度计算
# 读取内容关键词
import math
import jieba
import pandas as pd
import numpy as np
import jieba.analyse

# 从MySQL数据库的数据表中读取每一行数据放入列表中，最后返回一个完整的列表
import pymysql

#余弦相似度
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
        for j in range(len(wordlist)):
            print(wordlist[i],wordlist[j])
            simi = semDegree(wordlist[i], wordlist[j])
            semword[i][j] = format(simi, '.3f')

    return semword



def semDegree(s1, s2):
    s1_cut = [i for i in jieba.cut(s1, cut_all=True) if i != '']
    s2_cut = [i for i in jieba.cut(s2, cut_all=True) if i != '']

    word_set = set(s1_cut).union(set(s2_cut))
    word_dict = dict()
    i = 0
    for word in word_set:
        word_dict[word] = i
        i += 1

    s1_cut_code = [word_dict[word] for word in s1_cut]
    s1_cut_code = [0] * len(word_dict)

    for word in s1_cut:
        s1_cut_code[word_dict[word]] += 1

    s2_cut_code = [word_dict[word] for word in s2_cut]
    s2_cut_code = [0] * len(word_dict)
    for word in s2_cut:
        s2_cut_code[word_dict[word]] += 1

    # 计算余弦相似度
    sum = 0
    sq1 = 0
    sq2 = 0
    for i in range(len(s1_cut_code)):
        sum += s1_cut_code[i] * s2_cut_code[i]
        sq1 += pow(s1_cut_code[i], 2)
        sq2 += pow(s2_cut_code[i], 2)

    result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 2)
    return result


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
    for row in res:
        row = str(row).replace(" ", "")
        row = str(row).replace("/", "")
        wordlist.append(row)
    print(wordlist)


    semword = wordsim(wordlist)
    print(semword)
    data_df = pd.DataFrame(semword)
    # 将文件写入excel表格中
    writer = pd.ExcelWriter('contentyuxian.xlsx')  # 关键2，创建excel表格
    data_df.to_excel(writer, 'page_1',
                     float_format='%.3f')  # 关键3，float_format 控制精度，将data_df写到hhh表格的第一页中。若多个文件，可以在page_2中写入
    writer.save()  # 关键4
