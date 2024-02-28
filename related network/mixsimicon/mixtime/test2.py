#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> test2
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/11/11 11:20
@Desc   ：
=================================================='''
import requests

from mixsimicon.mixcon.simicon import simichnzn

sim=simichnzn("ATMOSPHERIC TEMPERATURE, ATMOSPHERIC RADIATION, ATMOSPHERIC PRESSURE, ATMOSPHERIC WATER VAPOR, ATMOSPHERIC WINDS WATER VAPOR INDICATORS, WIND DYNAMICS, SOLAR RADIATION, SURFACE TEMPERATURE",
              "ECOLOGICAL DYNAMICS, VEGETATION ECOSYSTEM FUNCTIONS, BIOMASS")
# sen1:大气温度、大气辐射、大气压力、大气水蒸气、大气风水蒸气指标、风力学、太阳辐射、地表温度
# sen2:生态动力学， 植被生态系统功能， 生物量
print(sim) #0.7619423270225525