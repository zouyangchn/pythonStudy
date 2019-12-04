from email.mime.text import MIMEText
# 最简单的纯文本邮件
# MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')


# 输入Email地址和口令:
# from_addr = input('From: ')
# password = input('Password: ')

from_addr1='PRD-Yang.Zou@winwayworld.com'
password1 = 'Zy123456'
# 输入收件人地址:
# to_addr = input('To: ')
to_addr1 = 'PRD-Yang.Zou@winwayworld.com'
# 输入SMTP服务器地址:
# smtp_server = input('mail.')
smtp_server1 = 'mail.Winwayworld.com'

import smtplib
server = smtplib.SMTP(smtp_server1, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr1, password1)
server.sendmail(from_addr1, [to_addr1], msg.as_string())
server.quit()