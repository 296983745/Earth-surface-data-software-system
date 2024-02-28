#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> test1207
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/12/7 15:19
@Desc   ：
# =================================================='''
# import numpy as np
# import pandas as pd
# from text2vec import SentenceModel, semantic_search
# from rdflib import Graph, Namespace
# data = pd.read_excel('subclass.xlsx')
# # embedder = SentenceModel("D:\\01study\\paraphrase-multilingual-MiniLM-L12-v2")
# embedder = SentenceModel("D:\\01study\\text2vec-base-multilingual")
# # 提取第一列与"subClassOf"相对应的数据
# corpus = data.iloc[:, 0].tolist()
# # 打印结果
# print(corpus)
# corpus_embeddings = embedder.encode(corpus)
# query_embedding = embedder.encode("海洋光学")
# hits = semantic_search(query_embedding, corpus_embeddings, top_k=1)
# hits = hits[0]
# print("\n\n======================\n\n")
# owlstr1 = corpus[hits[0]['corpus_id']]
# print(owlstr1)

import numpy as np
from scipy import stats

res=stats.spearmanr([3, 5, 1, 6, 7, 2, 8, 9, 4], [5, 3, 2, 6, 8, 1, 7, 9, 4])

print(res)