#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> timeEng
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/9/20 15:53
@Desc   ：
=================================================='''
from content.content_yuyi.simi_yuxian import get_mysql_list

if __name__ == '__main__':
    # 从数据库中取元素
    beginTime = get_mysql_list('earthdata', 'nasa1', 'Beginning_Date_Time')
    endTime = get_mysql_list('earthdata', 'nasa1', 'Ending_Date_Time')

    print(beginTime)
    print(endTime)

    # print(x)
