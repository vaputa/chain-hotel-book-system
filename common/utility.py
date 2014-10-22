#-*-coding:utf-8-*- 

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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

if __name__=='__main__':
	mailcontent='''
		<!DOCTYPE HTML>
		<html>
		<head>
		<meta charset="utf-8">
		<title>酒店注册验证</title>
		</head>
		<body>
			<h1>昊神太强了</h1>
		</body>
		</html>

	'''
	mysub="昊神灯全亮"
	send_mail("11300240039@fudan.edu.cn;11300240033@fudan.edu.cn",mysub,mailcontent)
