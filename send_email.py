import re
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subkect, msg_body, recipient):
	#sender information
    addr= 'nsbehackathon2014@gmail.com'
    username = 'nsbehackathon2014@gmail.com'
    password = 'nsbehackathon'

    #email information
    fromaddr = '<'+addr+'>'
    toaddr = '<'+recipient+'>'
    replyto = fromaddr
    msgsubject = subject
    sendtime = time.strftime("%b %d %Y at %H:%M:%S",time.localtime())
    htmlmsgtext = msg_body +'</br></br></br>' + '<br>' + sendtime

    try:
        msgtext = htmlmsgtext.replace('<b>','').replace('</b>','').replace('<br>',"\r").replace('</br>',"\r").replace('<br/>',"\r").replace('</a>','')
        msgtext = re.sub('<.*?>','',msgtext)

        msg = MIMEMultipart()
        msg.preamble = 'This is a multi-part message in MIME format.\n'
        msg.epilogue = ''

        body = MIMEMultipart('alternative')
        body.attach(MIMEText(msgtext))
        body.attach(MIMEText(htmlmsgtext, 'html'))
        msg.attach(body)
    
    
        msg.add_header('From', fromaddr)
        msg.add_header('To', toaddr)
        msg.add_header('Subject', msgsubject)
        msg.add_header('Reply-To', replyto)
   
 
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.set_debuglevel(False) #commenting this out, changing to False will make the script give NO output at all upon successful completion
    
        server.starttls()
        server.login(username,password)
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
    
        server.quit() 

    except:
        print ('Email NOT sent to %s successfully. %s ERR: %s %s %s ', str(toaddr), 'tete', str(sys.exc_info()[0]), str(sys.exc_info()[1]), str(sys.exc_info()[2]) )


#test purpose
if __name__ == '__main__':
    subject = 'Email Subject'
    msg_body = 'This is a test e-mail'
    recipient = 'nsbehackathon2014@gmail.com'
    send_email(subject, msg_body, recipient)