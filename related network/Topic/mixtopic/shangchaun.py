#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> shangchaun
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/11/29 18:41
@Desc   ：
=================================================='''
from neo4j import GraphDatabase
import csv

# 连接到 Neo4j 数据库
uri = "bolt://localhost:7687"  # 替换为实际的数据库 URI
username = "neo4j"  # 替换为实际的用户名
password = "123456"  # 替换为实际的密码

driver = GraphDatabase.driver(uri, auth=(username, password))

# 读取 CSV 文件并将数据存入 Neo4j
def import_csv_to_neo4j(file_path):
    with driver.session() as session:
        # 创建约束，确保节点的唯一性
        session.run("CREATE CONSTRAINT ON (n:Node) ASSERT n.id IS UNIQUE")

        # 读取 CSV 文件
        with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # 跳过标题行

            # 逐行导入数据
            for row in reader:
                subject, predicate, obj, *_ = row

                if predicate in ["type", "hasChineseName", "source", "comment","topic","altLabel"]:
                    # 创建或更新节点属性
                    set_property_query = (
                        f"MERGE (n:Node {{id: $subject}}) "
                        f"SET n.{predicate} = $obj"
                    )
                    session.run(set_property_query, subject=subject, obj=obj)
                else:
                    # 创建关系
                    create_relationship_query = (
                        "MERGE (s:Node {id: $subject}) "
                        "MERGE (o:Node {id: $obj}) "
                        "MERGE (s)-[r:RELATIONSHIP {predicate: $predicate}]->(o)"
                    )
                    session.run(create_relationship_query, subject=subject, predicate=predicate, obj=obj)

    print("数据导入完成！")

# 调用函数导入 CSV 数据到 Neo4j
csv_file_path = 'owlface.csv'  # 替换为实际的 CSV 文件路径
import_csv_to_neo4j(csv_file_path)