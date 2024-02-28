#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> mintopictest
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/11/29 15:18
@Desc   ：计算nasa 的主题相关度，直接将其存入三元组，再计算名字和本体最相似度的进行链接，也存入三元组
=================================================='''
import pandas as pd
import pandas as pd
from text2vec import Similarity, SentenceModel, semantic_search

from content.content_yuyi.simi_hownet import get_mysql_list
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import difflib
import openpyxl
from text2vec import Similarity
def compute_similarity(words1, words2):
    # 将两组单词转换为字符串
    str1 = ' '.join(words1)
    str2 = ' '.join(words2)

    # 计算Levenshtein距离
    distance = difflib.SequenceMatcher(None, str1, str2).ratio()

    return distance
from content.content_yuyi.simi_yuxian import get_mysql_list

if __name__ == '__main__':
    sim_model = Similarity("D:\\01study\\paraphrase-multilingual-MiniLM-L12-v2")
    entry_Title= get_mysql_list('earthdata', 'engnasa', 'Entry_Title')
    category = get_mysql_list('earthdata', 'engnasa', 'Category')
    topic = get_mysql_list('earthdata', 'engnasa', 'Topic')
    term = get_mysql_list('earthdata', 'engnasa', 'Term')
    variable_Level_1 = get_mysql_list('earthdata', 'engnasa', 'Variable_Level_1')

    variable_Level_1similarity=0
    topicsimilarity=0
    termsimilarity=0
    new_data = []
    new_data2=[]
    for i in range(len(entry_Title)):
        new_row = {
            'Subject': entry_Title[i][0],
            'Predicate': "topic",
            'Object': category[i][0]+","+topic[i][0]+","+term[i][0]+","+variable_Level_1[i][0]
        }
        new_data.append(new_row)
    for i in range(len(entry_Title)):
        for j in range(i + 1, len(entry_Title)):
            # 在这里执行您的操作，使用 i 和 j 来访问 entry_Title 中的元素或执行其他操作   sim_model.get_scores()
            simi=0;
            if category[i][0]==category[j][0]:
                simi+=0.25;
                topicsimilarity =sim_model.get_scores(topic[i][0],topic[j][0])
                topicsimilarity=topicsimilarity[0][0]
                topicsimilarity/=4;
                if topicsimilarity>0.12:
                    simi+=topicsimilarity
                    termsimilarity = sim_model.get_scores(term[i][0], term[j][0])
                    termsimilarity=termsimilarity[0][0]
                    termsimilarity/=4;
                    if termsimilarity>0.12:
                        simi+=termsimilarity
                        variable_Level_1similarity = sim_model.get_scores(variable_Level_1[i][0], variable_Level_1[j][0])
                        if len(variable_Level_1similarity) > 0:
                            variable_Level_1similarity=variable_Level_1similarity[0][0]
                            variable_Level_1similarity/=4
                            if variable_Level_1similarity>0.12:
                                simi+=variable_Level_1similarity
                else:
                    simi+=topicsimilarity
            else:
                simi=0
            if simi>0.5:
                #存入name1,topic,name2
                new_row = {
                    'Subject': entry_Title[i][0],
                    'Predicate': "topic" + str(simi),
                    'Object': entry_Title[j][0]
                }
                new_data2.append(new_row)

    embedder = SentenceModel("D:\\01study\\paraphrase-multilingual-MiniLM-L12-v2")

    data = pd.read_csv('owlface.csv')

    # 提取第一列与"subClassOf"相对应的数据
    corpus = data[data.iloc[:, 1] == 'subClassOf'].iloc[:, 0].tolist()
    # 打印结果
    print(corpus)
    corpus_embeddings = embedder.encode(corpus)
    for i in range(len(entry_Title)):
        string=variable_Level_1[i][0]
        query_embedding = embedder.encode(string)
        hits = semantic_search(query_embedding, corpus_embeddings, top_k=1)
        hits = hits[0]
        print("\n\n======================\n\n")
        new_row = {
            'Subject': entry_Title[i][0],
            'Predicate': "belong",
            'Object': corpus[hits[0]['corpus_id']]
        }
        new_data.append(new_row)



    df = pd.read_csv('owlface1202.csv')

    # 创建新的 DataFrame
    new_rows = pd.DataFrame(new_data)

    # 将新数据插入到 DataFrame 的末尾
    df = pd.concat([df, new_rows], ignore_index=True)

    # 将数据保存到 CSV 文件
    df.to_csv('owlface.csv', index=False)
    print('finish')




