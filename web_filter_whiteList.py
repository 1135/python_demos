#! /usr/bin/env python
# coding=utf-8

import re

#白名单法【安全】

def Check(input_from_user):
    regex_ = '[^0-9|a-z|A-Z|._]' # 如果存在 白名单字符 0-9|a-z|A-Z|._ 以外的字符则return 0
    result_list2 = re.findall(regex_,long_str_from_user,re.MULTILINE)# re.MULTILINE多行模式

    if len(result_list2):
        print '发现特殊字符'+str(result_list2)
        return 0
    else:
        return 1


if __name__ == '__main__':

    # 如 含有换行符号 不符合白名单规则
    long_str_from_user = """
    test\/
    ~!@$%^*(#%&*
    """

    if Check(long_str_from_user) == 0:
        print "不符合白名单规则"
