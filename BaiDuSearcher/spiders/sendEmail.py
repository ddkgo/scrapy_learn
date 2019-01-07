import zmail

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
from_addr = 'ouzhengai@hotmail.com'   # 邮箱登录用户名
password  = 'Oz1314520'              # 登录密码
#to_addr   = ['740462016@qq.com','jason1423@vip.qq.com','jason14449905@126.com']      # 发送对象地址，可以多个邮箱
smtp_server='smtp.live.com'          # 服务器地址，默认端口号25

class SendEmail():

    '''加密发送文本邮件'''
    def sendEmail(self,to_addr):
        try:
            # 你的邮件内容
            mail_content = {
                'subject': '[BIKE] A new welcome bike',  # 随便填写
                'content_text': '''It's a mullet—a sexy, sexy mullet. 
                At first glance, this bike is all business. Short-travel. Carbon all-the-things. A rawboned 5.5-pound frame. 
                If you're looking at suspension numbers alone, this is a straight-XC rig. 
                After all, bikes with 100 millimeters of rear travel usually come with a heart-rate monitor and training zones
                that don't involve riding until you taste the pizza you ate for breakfast.''',  # 随便填写
            }
            server = zmail.server(from_addr, password)  # 登录邮箱服务器
            server.send_mail([to_addr], mail_content) # 发送信息
            print("邮件发送成功！")
            return True
        except Exception as e:
            print("发送失败：" + e)
            return False


    '''发送带图片附件的邮件'''
    def sendFileEmail(self,to_addr):
        try:
            msg =  MIMEMultipart()
            msg['From'] = _format_addr('信息化工程所 <%s>' % from_addr)
            msg['To'] = _format_addr('收件人 <%s>' % to_addr)
            msg['Subject'] = Header('邮件的主题：问候', 'utf-8').encode()
            # 邮件正文是MIMEText:
            msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
            # msg.attach(MIMEText('<html><body><h1>你好</h1>' + '<p>send by <img src=cid:0"></p>' +'</body></html>', 'html', 'utf-8')) # 网页文件


            # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
            with open(r'./file/图片.png', 'rb') as f:
                mime = MIMEBase('image', 'png', filename='图片.png') # 设置附件的MIME和文件名，这里是png类型:
                mime.add_header('Content-Disposition', 'attachment',filename=('gbk', '', '图片.png')) # 加上必要的头信息,解决中文附件名乱码
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                mime.set_payload(f.read())  # 把附件的内容读进来:
                encoders.encode_base64(mime) # 用Base64编码:
                msg.attach(mime) # 添加到MIMEMultipart:

            server = zmail.server(from_addr, password)  # 登录邮箱服务器
            server.send_mail(to_addr, msg.as_string()) # 发送信息
            print("带图片邮件发送成功！")
        except Exception as e:
            print("发送失败：" + e)



    '''发送带图片附件的邮件'''
    def sendFilesEmail(self,to_addr):
        try:
            msg =  MIMEMultipart()
            msg['From'] = _format_addr('信息化工程所 <%s>' % from_addr)
            msg['To'] = _format_addr('收件人 <%s>' % to_addr)
            msg['Subject'] = Header('邮件的主题：问候', 'utf-8').encode()
            # 邮件正文是MIMEText:
            msg.attach(MIMEText('发送多附件邮件...', 'plain', 'utf-8'))

            #---这是附件部分---
            #xlsx类型附件
            part = MIMEApplication(open(r'./file/foo.xlsx','rb').read())
            part.add_header('Content-Disposition', 'attachment', filename="foo.xlsx")
            msg.attach(part)

            #jpg类型附件
            part = MIMEApplication(open(r'./file/图片.png','rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=('gbk', '', '图片.png'))
            msg.attach(part)

            #pdf类型附件
            part = MIMEApplication(open(r'./file/foo.pdf','rb').read())
            part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")
            msg.attach(part)

            # #mp3类型附件
            # part = MIMEApplication(open('foo.mp3','rb').read())
            # part.add_header('Content-Disposition', 'attachment', filename="foo.mp3")
            # msg.attach(part)

            # server.set_debuglevel(1) # 记录详细信息
            server = zmail.server(from_addr, password) # 登录邮箱服务器
            server.send_mail(to_addr, msg.as_string()) # 发送信息
            print("带图片邮件发送成功！")
        except Exception as e:
            print("发送失败：" + e)
