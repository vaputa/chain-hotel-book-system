#-*-coding:utf-8-*- 

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import time
import hashlib
import random
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')

mail_host="smtp.163.com"
mail_user="godhaohotel@163.com"
mail_pass="hotelhaogod"

#接口 第一个参数是收件人地址，第二个是邮件标题，第三个是内容
def send_mail(to_list,sub,content):        
	me=mail_user
	msg=MIMEText(content,_subtype='html',_charset='utf-8')
	if not isinstance(sub,unicode):
		sub=unicode(sub)
	msg['Subject']=sub
	msg['From']=me
	#msg=";".join(to_list)
	msg['To']=to_list
	try:
		s=smtplib.SMTP()
		s.connect(mail_host)
		s.login(mail_user,mail_pass)
		s.sendmail(me,to_list.split(';'),msg.as_string())
		s.close()
		return True
	except Exception,e:
		print str(e)
		return False

def generateToken():
	#以下为md5的url生成部分，通过当前时间戳和一个随机数确定一个字符串，对其进行md5处理
	d=time.time()
	t=random.random()
	unistr=str(d+t)
	mymd5=hashlib.md5()
	mymd5.update(unistr)
	link=mymd5.hexdigest()
	return link



