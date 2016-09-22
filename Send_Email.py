# coding:utf-8 #

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(),
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

# from_addr = 'qiujiayu0212@163.com' # raw_input('From: ')
# password = 'yingming0403' # raw_input('Password: ')
# to_addr = ['sohu.321@qq.com', '3607442@qq.com'] # raw_input('To: ')
# smtp_server = 'smtp.163.com' # raw_input('SMTP server: ')

# to_addr类型为list


def send_email(to_addr, warning_str, subject_str,
               from_addr='qiujiayu0212@163.com',
               password='yingming0403',
               smtp_server='smtp.163.com'):

    for x in to_addr:
        print x
        print subject_str
        msg = MIMEText(warning_str, 'plain', 'utf-8')
        msg['From'] = _format_addr(u'来自邱家瑜的python <%s>' % from_addr)
        msg['To'] = _format_addr(u'管理员 <%s>' % x)
        try:
            msg['Subject'] = Header(u"%s" % subject_str, 'utf-8').encode()
        except:
            print "error subject"
            msg['Subject'] = Header(u"from qiu's python", 'utf-8').encode()

        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [x], msg.as_string())
        server.quit()

        print 'send success!'
