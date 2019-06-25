import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
import config_file


port = 465
smtp_server = 'smtp.gmail.com'
sender_email = config_file.custom_email 
receiver_email = [] # input email
password = config_file.email_password 



message = MIMEMultipart("alternative")
message["Subject"] = "THIS IS NOT SPAM"
message["From"] = sender_email
message["To"] = ', '.join(receiver_email)

text = """Please click this very unsuspicious link -> lainofthewired.pythonanywhere.com\nYour password is: fren"""
html = """\
<html>
    <body>
        <p>Please click this very unsuspicious link -> <a href='lainofthewired.pythonanywhere.com'>lainofthewired.pythonanywhere.com</a></p>
        <p>Your password is: fren</p> 
    </body>
</html>"""


part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()

server = smtplib.SMTP_SSL(smtp_server, port)
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message.as_string())
server.quit()
print('it works')

