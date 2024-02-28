#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> transerformtest
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/11/12 17:24
@Desc   ：
=================================================='''
from Time.TimeSimi import TimeRela


class MyClass:
    def __init__(self, Begine, End):
        self.Begine = Begine
        self.End = End


x=MyClass(2020,2021)
y=MyClass(2020,2020)
simi = TimeRela(y,x)
print(simi)
