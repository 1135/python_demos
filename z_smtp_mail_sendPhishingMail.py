#!/usr/bin/env python
# encoding: utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header


# SPF介绍
# SPF是为了防范垃圾邮件而提出来的一种DNS记录类型，它是一种TXT类型的记录，它用于登记某个域名拥有的用来外发邮件的所有IP地址。
# 按照SPF的格式在DNS记录中增加一条TXT类型的记录，将提高该域名的信誉度，同时可以防止垃圾邮件伪造该域的发件人发送垃圾邮件。
# SPF是跟DNS相关的一项技术，它的内容写在DNS的txt类型的记录里面。
# mx记录的作用是给寄信者指明某个域名的邮件服务器有哪些。
# SPF的作用跟mx相反，它向收信者表明，哪些邮件服务器是经过某个域名认可的会发送邮件的。

#实测
# 伪造发件邮箱地址  收件邮箱   收件邮箱是否收到
# xxx@126.com    126邮箱   正常收件
# xxx@qq.com     126邮箱   正常收件
# xxx@xxx.com    126邮箱   正常收件
# xxx@sohu.com   sohu邮箱  正常收件
# xxx@xxx.com    sohu邮箱  正常收件
# xxx@xxx.com    QQ邮箱    会识别真实的发件地址
# 可测试自己公司是否能识别此类伪造邮件。

def send_mail_sohu(from_addrs,to_addrs,mail_Subject, mail_content,type='plain'):
    _user = 'user@sohu.com'
    _pwd = 'pass'

    # 使用MIMEText构造符合smtp协议的header及body
    msg = MIMEText(mail_content, type, 'utf-8')
    msg["Subject"] = Header(mail_Subject, 'utf-8')
    msg["From"] = Header(from_addrs,)#'utf-8')  # 发件人
    msg["To"] = ",".join(to_addrs)

    try:
        s = smtplib.SMTP("smtp.sohu.com", timeout=30)  # 连接smtp邮件服务器,默认端口25
        s.login(_user, _pwd)  # 登陆服务器
        s.sendmail(_user, to_addrs, msg.as_string())  # 发送邮件
    except Exception as e:
        print "mail error\n" + str(e)

if __name__ == '__main__':
    from_addrs = '<sender@126.com>' # 伪造发件人地址
    to_addrs = [ 'recevice@sohu.com','recevice@126.com'] # 收件人列表 群发不密送

    send_mail_sohu(from_addrs,to_addrs, 'sub', "text", "plain")
    
#从收件箱导出的.eml文件内容如下
"""
Return-Path: <我的收件箱@sohu.com>
X-Original-To: 我的收件箱@sohu.com
Delivered-To: 我的收件箱@sohu.com
Received: from smtp_68_108 (unknown [10.16.68.108])
	by mx208.mail.sohu.com (Postfix) with ESMTP id 21C5E9602F6
	for <我的收件箱@sohu.com>; Wed, 17 Oct 2018 11:25:18 +0800 (CST)
Received: from wdeMacBook-Pro.local (unknown [我的外网ip])
	by smtp_68_108 (Postfix) with ESMTPA id 42ZcxZ5z11z41xp;
	Wed, 17 Oct 2018 11:25:06 +0800 (CST)
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: base64
Subject: =?utf-8?q?sub?=
From: <sender@126.com>
To: 我的收件箱@sohu.com,arr0w1@126.com
X-Sohu-Gateway: 1
X-Sohu-Antispam-Language: 0
X-Sohu-Antispam-Score: 1.15710189566

dGV4dA==

"""
