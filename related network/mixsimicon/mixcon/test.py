#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> test
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/11/12 21:18
@Desc   ：
=================================================='''

from transformers import AutoTokenizer, AutoModel
import torch

from text2vec import SentenceModel, cos_sim, Similarity, SimilarityType, EmbeddingType,CosentModel

# Two lists of sentences
sentences1 = ['如何更换花呗绑定银行卡',
              'The cat sits outside',
              'A man is playing guitar',
              'The new movie is awesome']

sentences2 = ['花呗更改绑定银行卡',
              'The dog plays in the garden',
              'A woman watches TV',
              'The new movie is so great']
# sim_model = Similarity("D:\\01study\\paraphrase-multilingual-MiniLM-L12-v2")

sim_model = Similarity("D:\\01study\\text2vec-base-multilingual")
# sim_model = Similarity("D:\\01study\\01python_item\sentence-transformers-master\sentence-transformers-master\examples\\training\\nli\output\\training_nli_paraphrase-multilingual-MiniLM-L12-v2-2023-11-16_10-09-54")
# 纯中文建议使用模型"shibing624/text2vec-base-chinese"，
# 多语言建议使用模型"sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

# scores = sim_model.get_scores("The land is covered with 30m resolution artificial surface land", "土地覆被   30m分辨率   人工表面用地")
# print(scores[0][0])
#
#
# scores = sim_model.get_scores("陕西省   1:400万   县级   行政区划   1995年 "," 广东省   1:400万   县级   行政区划   1984年")
# print(scores[0][0])
#
#
# print(sim_model.model)
print(sim_model.__str__())


#中英文测试
sim=sim_model.get_scores("The land is covered with 30m resolution artificial surface land","土地覆被   30m分辨率   人工表面用地")

print(sim[0][0]) #0.9413836598396301

#相似中文测试
sim=sim_model.get_scores("陕西省   1:400万   县级   行政区划   1995年 "," 广东省   1:400万   县级   行政区划   1984年")
print(sim[0][0]) #0.9225271344184875

#完全不同中文测试
sim=sim_model.get_scores("土地覆被   林地   遥感解译 "," 广东省   1:400万   县级   行政区划   1984年")
print(sim[0][0]) #0.8013457655906677


#较相似英文文本测试
sim=sim_model.get_scores("ATMOSPHERIC TEMPERATURE, ATMOSPHERIC RADIATION, ATMOSPHERIC PRESSURE, ATMOSPHERIC WATER VAPOR, ATMOSPHERIC WINDS WATER VAPOR INDICATORS, WIND DYNAMICS, SOLAR RADIATION, SURFACE TEMPERATURE",
              " ATMOSPHERIC TEMPERATURE, PRECIPITATION, OCEAN WINDS, SALINITY/DENSITY, OCEAN CIRCULATION, OCEAN TEMPERATURE, OCEAN PRESSURE, ATMOSPHERIC RADIATION, OCEAN HEAT BUDGET, ATMOSPHERIC WATER VAPOR, CLOUDS, ATMOSPHERIC WINDS INCOMING SOLAR RADIATION, FRESH WATER FLUX, SHORTWAVE RADIATION, NET RADIATION, SEA LEVEL PRESSURE, OUTGOING LONGWAVE RADIATION, ABSORPTION, SURFACE TEMPERATURE, SOLAR RADIATION, SALINITY, CLOUD PROPERTIES, SURFACE WINDS, PRECIPITATION AMOUNT, OCEAN MIXED LAYER, WATER VAPOR INDICATORS, LONGWAVE RADIATION, HEAT FLUX")
# sen1:大气温度、大气辐射、大气压力、大气水蒸气、大气风水蒸气指标、风力学、太阳辐射、地表温度
# sen2: 大气温度、降水、海风、盐度/密度、海洋环流、海洋温度、海洋压力、大气辐射、海洋热收支、大气水蒸气、云、大气风、入射太阳辐射、淡水通量、短波辐射、净辐射、海平面压力、出射长波辐射、吸收、地表温度、太阳辐射、盐度、云属性、地表风、降水量、海洋混合层、水蒸气指示器、长波辐射、热通量
print(sim[0][0]) #0.9234554767608643

#完全不同英文文本测试
sim=sim_model.get_scores("ATMOSPHERIC TEMPERATURE, ATMOSPHERIC RADIATION, ATMOSPHERIC PRESSURE, ATMOSPHERIC WATER VAPOR, ATMOSPHERIC WINDS WATER VAPOR INDICATORS, WIND DYNAMICS, SOLAR RADIATION, SURFACE TEMPERATURE",
              "ECOLOGICAL DYNAMICS, VEGETATION ECOSYSTEM FUNCTIONS, BIOMASS")
# sen1:大气温度、大气辐射、大气压力、大气水蒸气、大气风水蒸气指标、风力学、太阳辐射、地表温度
# sen2:生态动力学， 植被生态系统功能， 生物量
print(sim[0][0]) #0.7619423270225525
# print('1:use Similarity compute cos scores\n')
# for i in range(len(sentences1)):
#     for j in range(len(sentences2)):
        # print("{} \t\t {} \t\t Score: {:.4f}".format(sentences1[i], sentences2[j], scores[i][j]))


# CosentModel
# [[0.9301533]]
# [[0.84255254]]
# [[0.30777746]]
# [[0.82586086]]
# [[0.21762261]]


sim=sim_model.get_scores("OCEAN CIRCULATION","Ocean")
print(sim[0][0]) #0.8013457655906677