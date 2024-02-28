#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> damoxing
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/12/23 10:09
@Desc   ：使用大模型判断地理空间位置相似的

=================================================='''
import pandas as pd
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

from content.content_yuyi.simi_yuxian import get_mysql_list

task = Tasks.sentence_similarity
model = 'damo/mgeo_geographic_entity_alignment_chinese_base'
# inputs = inputs = ('黄河流域', '中国北方10省区及西南四川省')
x = get_mysql_list('earthdata', 'datatopic', 'SpacePlc')
print(x)
# inputs=[]
results = []
pipeline_ins = pipeline(
    task=task, model=model, model_revision='v1.2.0')
for i in range(len(x)):
    for j in range(i+1,len(x)):
        res=pipeline_ins(input=(x[i][0],x[j][0]))
        print(res)
        results.append((x[i][0], x[j][0], res))




# 创建一个DataFrame对象
df_results = pd.DataFrame(results, columns=['输入1', '输入2', '处理结果'])
# 将DataFrame保存为Excel文件
df_results.to_excel('results.xlsx', index=False)


# # {'scores': [0.7280762195587158, 0.16257540881633759, 0.109348364174366], 'labels': ['partial_match', 'not_match', 'exact_match']}
# # 部分匹配'、'不匹配'、'完全匹配
