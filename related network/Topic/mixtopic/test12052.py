#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> test12052
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/12/5 22:11
@Desc   ：最近父节点算法

=================================================='''

# import pandas as pd
#
# def build_tree(df):
#     tree = {}
#     for row in df.itertuples(index=False):
#         child = row[0]
#         parent = row[2]
#         if child not in tree:
#             tree[child] = []
#         if not pd.isna(parent):
#             tree[child].append(parent)
#     return tree
#
# def find_common_parent(tree, node1, node2):
#     path1 = find_path(tree, node1)
#     path2 = find_path(tree, node2)
#     print(path1)
#     print("000")
#     print(path2)
#     print("000")
#     if path1 is None or path2 is None:
#         return None
#     for i in range(min(len(path1), len(path2))):
#         if path1[i] != path2[i]:
#             return path1[i-1]
#     return path1[min(len(path1), len(path2)) - 1]
#
# def find_path(tree, node):
#     path = []
#     while node in tree:
#         path.append(node)
#         node = tree[node][0]
#     return path[::-1] if path else None
#
# # 读取Excel文件
# df = pd.read_excel('subclassof.xlsx', header=None)
#
# # 构建树结构
# tree = build_tree(df)
#
# node1 = 'HalogenatedHydrocarbonsAndHalogens'
# node2 = 'NearEarthSpaceLayer'
#
# common_parent = find_common_parent(tree, node1, node2)
from rdflib import Graph, Namespace
from rdflib.namespace import RDFS

def calculate_distances(node1_uri, node2_uri):
    # 创建RDF图
    graph = Graph()

    # 解析RDF数据
    rdf_file = "D:\\neo4j-community-3.5.14\\import\\EarthSurfaceSystem.rdf"  # 替换为实际的RDF文件路径
    graph.parse(rdf_file, format="xml")  # 根据实际的文件格式选择适当的解析器

    # 定义命名空间
    ns = Namespace("http://www.semanticweb.org/ontologies/202310/earthsurfacesystem#")

    # 定义两个子节点
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
    print(path1)
    print(path2)
    print(lca)
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

# 用法示例
node1_uri = "NaturalEcosystem"
node2_uri = "OceanOpticalDepth"
node1_distance, node2_distance, lca_to_root_distance = calculate_distances(node1_uri, node2_uri)
if node1_distance is not None and node2_distance is not None and lca_to_root_distance is not None:
    print("节点1到最近公共父节点的距离:", node1_distance)
    print("节点2到最近公共父节点的距离:", node2_distance)
    print("最近公共父节点到根节点的距离:", lca_to_root_distance)
else:
    print("没有找到最近公共父节点")