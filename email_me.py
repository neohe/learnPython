#!/usr/bin/env python
# -*- coding: utf-8 -*-

import email
import smtplib

from_addr = 'heyong2007@163.com'
to_addr = 'heyong2007@163.com'
smtp_server =  'smtp.163.com'

msg =  email.MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] =  Header(u'邮件',  'utf-8').encode()
msg.attach(MIMEText('Sent by Python',  'plain',  'utf-8'))

with open('compile.log', 'rb')  as f:
    # 附件信息
    mime = MIMEBase('text',  'log', filename =  'compile.log')
    # 加上必要的头信息
    mime.add_header()
    # 读取附件内容
    mine.set_payload(f.read())
    # Base64 编码
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.login('heyong2007@163.com',  'hey290274')
server.sendmail(from_addr, [to_addr],  msg.as_string())
server.quit()
