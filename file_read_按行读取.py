#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 读文件 按行读
#python2 测试可用

for x in open('a.txt'):
        a = x.replace('\n', '')
        print(a)#因为print函数会自动输出换行符 所以把文本原有的\n替换为空后的输出看起来是常规的，否则会多出空行


"""
aaaaaaa
bbbbb
ccc
d
"""

#################

# 把文件每一行 作为列表元素 全都加入列表
# [line.strip("\r").strip("\n").strip() for line in f.readlines()]
