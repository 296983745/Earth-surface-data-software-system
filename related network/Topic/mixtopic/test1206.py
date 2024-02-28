#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> test1206
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/12/6 11:00
@Desc   ：
=================================================='''
import numpy as np
import pandas as pd
from text2vec import SentenceModel, semantic_search

from content.content_yuyi.simi_hownet import get_mysql_list
from mixsimicon.mixcon.simicon import sim_model
import pandas as pd
from rdflib import Graph, Namespace
data = pd.read_excel('subclass.xlsx')
embedder = SentenceModel("D:\\01study\\text2vec-base-multilingual")
# 提取第一列与"subClassOf"相对应的数据
corpus = data.iloc[:, 0].tolist()
# 打印结果
print(corpus)
corpus_embeddings = embedder.encode(corpus)
query_embedding = embedder.encode("OCEAN CHEMISTRY")
hits = semantic_search(query_embedding, corpus_embeddings, top_k=1)
hits = hits[0]
print("\n\n======================\n\n")
owlstr1 = corpus[hits[0]['corpus_id']]
print(owlstr1)