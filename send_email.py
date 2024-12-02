import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, body, to_email):
    msg = MIMEMultipart()
    msg['From'] = '790114980@qq.com'
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('mail.qq.com', 587)
    server.starttls()
    server.login('790114980@qq.com', 'Zcheng19890424!')
    text = msg.as_string()
    server.sendmail('790114980@qq.com', to_email, text)
    server.quit()


if __name__ == '__main__':
    send_email('Aloha!', 'Aloha world!', '18761691890@163.com')
