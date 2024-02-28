#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> hownet1229
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/12/29 15:23
@Desc   ：
=================================================='''
import OpenHowNet
# OpenHowNet.download()
hownet_dict_advanced = OpenHowNet.HowNetDict(init_sim=True)

hownet_dict_advanced.initialize_similarity_calculation()
simi=hownet_dict_advanced.calculate_word_similarity('地表覆盖','地表覆被')
print(simi)