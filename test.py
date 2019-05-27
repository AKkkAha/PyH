#!/usr/bin/python
#-*- encoding:UTF-8 -*-
from Html import *

#obj = Html("result")
#obj.parse_logfile("test.txt")

import os

# 输入目录路径，输出最新文件完整路径
def find_new_file(dir):
    '''查找目录下最新的文件'''
    file_lists = os.listdir(dir)
    file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn)
                    if not os.path.isdir(dir + "\\" + fn) else 0)
    print('最新的文件为： ' + file_lists[-1])
    file = os.path.join(dir, file_lists[-1])
    print('完整路径：', file)
    return file

# 函数调用
dir = os.getcwd()
find_new_file(dir)