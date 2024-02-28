#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> 1202test
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/12/2 20:01
@Desc   ：
=================================================='''
import numpy as np
from text2vec import SentenceModel, semantic_search
from content.content_yuyi.simi_hownet import get_mysql_list
import pandas as pd
from rdflib import Graph, Namespace
data = pd.read_excel('subclass.xlsx')
embedder = SentenceModel("D:\\01study\\text2vec-base-multilingual")
# 提取第一列与"subClassOf"相对应的数据
corpus = data.iloc[:, 0].tolist()
# 打印结果
print(corpus)
corpus_embeddings = embedder.encode(corpus)
# 创建RDF图
graph = Graph()

    # 解析RDF数据
rdf_file = "D:\\neo4j-community-3.5.14\\import\\EarthSurfaceSystem.rdf"  # 替换为实际的RDF文件路径
graph.parse(rdf_file, format="xml")  # 根据实际的文件格式选择适当的解析器

# 定义命名空间
ns = Namespace("http://www.semanticweb.org/ontologies/202310/earthsurfacesystem#")
def calculate_distances(node1_uri, node2_uri):
#定义两个子节点
    child1 = ns[node1_uri]
    child2 = ns[node2_uri]

    # SPARQL查询模板，获取节点的父节点
    query_template = """
    SELECT ?parent
    WHERE {{
      <{child_uri}> rdfs:subClassOf ?parent .
    }}
    """
    # 获取child1的路径
    path1 = []
    current_node = child1
    while True:
        path1.append(str(current_node))
        query = query_template.format(child_uri=current_node)
        results = graph.query(query)
        if len(results) > 0:
            for result in results:
                current_node = result.parent
                break
        else:
            break

    # 获取child2的路径
    path2 = []
    current_node = child2
    while True:
        path2.append(str(current_node))
        query = query_template.format(child_uri=current_node)
        results = graph.query(query)
        if len(results) > 0:
            for result in results:
                current_node = result.parent
                break
        else:
            break

    # 查找最近公共父节点
    lca = "http://www.w3.org/2002/07/owl#Thing"
    i = len(path1) - 1
    j = len(path2) - 1

    while i >= 0 and j >= 0:
        if path1[i] == path2[j]:
            lca = path1[i]
            i -= 1
            j -= 1
        else:
            break

    if lca:
        # 计算node1到最近公共父节点的距离

        # 计算最近公共父节点到根节点的距离
        lca_to_root_distance = len(path1) - path1.index(lca) - 1
        node1_distance = len(path1) -lca_to_root_distance - 1
        # 计算node2到最近公共父节点的距离
        node2_distance = len(path2) -lca_to_root_distance - 1
        return node1_distance, node2_distance, lca_to_root_distance

    else:
        return None, None, None
import pandas as pd
def calculate_similarity(node1_distance, node2_distance, lca_to_root_distance):
    numerator = lca_to_root_distance * 2
    denominator = node1_distance + node2_distance + lca_to_root_distance * 2
    if denominator != 0:
        similarity = numerator / denominator
        return similarity
    else:
        return 0.0  # 避免除以零的情况
def simimix(str1,str2):
    query_embedding = embedder.encode(str1)
    hits = semantic_search(query_embedding, corpus_embeddings, top_k=1)
    hits = hits[0]
    print("======================\n")
    owlstr1=corpus[hits[0]['corpus_id']]
    query_embedding = embedder.encode(str2)
    hits = semantic_search(query_embedding, corpus_embeddings, top_k=1)
    hits = hits[0]

    owlstr2 = corpus[hits[0]['corpus_id']]
    print(owlstr1)
    print(owlstr2)
    # //特征词，找到Excel中节点  owlstr1,owlstr2
    node1_distance, node2_distance, lca_to_root_distance = calculate_distances(owlstr1, owlstr2)
    simimintopic=0
    print(node1_distance)
    print(node2_distance)
    print(lca_to_root_distance)
    if node1_distance is not None and node2_distance is not None and lca_to_root_distance is not None:
        simimintopic=calculate_similarity(node1_distance, node2_distance, lca_to_root_distance)
    # 找到共同父节点。
    print(simimintopic)
    return simimintopic;
if __name__ == '__main__':
    entry_Title = get_mysql_list('earthdata', 'engnasa', 'Entry_Title')
    # variable_Level_1 = get_mysql_list('earthdata', 'engnasa', 'Variable_Level_1')
    # print(variable_Level_1)
    variable_Level_1 = get_mysql_list('earthdata', 'engnasa', 'Term')
    print(variable_Level_1)
    # 读取exceL本体树
    new_data = []
    for i in range(len(variable_Level_1)):
        for j in range(i+1,len(variable_Level_1)):
            parts = variable_Level_1[i][0].split(', ')
            parts2=variable_Level_1[j][0].split(', ')
            listi=[]
            for k in range(len(parts)):
                listii=[]
                for l in range(len(parts2)):
                    tmp=simimix(parts[k],parts2[l])
                    listii.append((tmp));
                listi.append(np.max(listii))
            resij=np.mean(listi)
            print(resij)
            print(variable_Level_1[i])
            print(variable_Level_1[j])


            # 假设 resij、variable_Level_1[i] 和 variable_Level_1[j] 是包含数据的列表或变量

            # 创建一个字典，包含要保存到Excel的数据
            new_row = {
                'data1': entry_Title[i][0],
                'data2': entry_Title[j][0],
                'simi': resij,
                'simii': variable_Level_1[i],
                'simij': variable_Level_1[j]
            }
            new_data.append(new_row)

    df = pd.read_csv('test1209Term.csv')

    # 创建新的 DataFrame
    new_rows = pd.DataFrame(new_data)

    # 将新数据插入到 DataFrame 的末尾
    df = pd.concat([df, new_rows], ignore_index=True)

    # 将数据保存到 CSV 文件
    df.to_csv('test1209Term.csv', index=False)
    print('finish')
# test1209Term 完整

