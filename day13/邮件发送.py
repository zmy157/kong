import smtplib
from email.mime.text import MIMEText # 文本
from email.mime.multipart import MIMEMultipart # 附件
from email.header import Header # 配置一些头信息

# SGHYLZUWHOCYIJOE   srbfgzpyoisaeaac  wzfkufnzpdtjdjfc
sender = "1572099050@qq.com"     # 发送人的邮件
recevises = ["2431320433@qq.com"] # 接收人列表，可以写多个
mail_host = "smtp.qq.com"       # smtp邮箱的服务器地址
password = "ipclunfappirfief"   # 本人邮件发送授权码
subject = "这是一封测试邮件"    # 本次邮件发送的主题

# message = MIMEText("这是一个计算器的测试邮件！！！","plain","utf-8")
message = MIMEMultipart()  # 附件管理器，能添加N多个附件
# 设置发送邮件的一些配置
message["From"] = Header("张明豫","utf-8")
message["TO"] = Header("测试","utf-8")
message["Subject"]  = Header(subject,"utf-8")

message.attach(MIMEText("这是附件","plain","utf-8"))
# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('计算器的报告.html', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment;filename="computer.html"'
message.attach(att1)

try:
    smtp  = smtplib.SMTP() # smtp 发送器
    smtp.connect(mail_host,587)
    smtp.login(sender,password)
    smtp.sendmail(sender,recevises,message.as_string())
    print("发送成功！")
except Exception as error:
    print("邮件发送失败！",error)




















