import smtplib
import ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from_email = "YOUR EMAIL"
to_email = "EMAIL ADDRESS TO SEND TO"

# Add your password in the password.txt file
with open("password.txt","r") as f:
    password = f.read()

# Build out the email
msg = MIMEMultipart()
msg['From'] = 'Humans of Mars'
msg['To'] =    to_email
msg['Subject'] = 'Testing 1 2 3 ...'

# Add message you wish to send in message.txt
with open("message.txt","r") as f:
    message = f.read()

# message must be converted to a MIMEText object before attaching to the msg object
msg.attach(MIMEText(message,'plain'))

# //////////// ATTACHING AN IMAGE TO OUR EMAIL ///////////////////////////////////
# Image attachment
filename = "Django-Image.jpg"
attachment = open(filename,"rb")

# process image data
p = MIMEBase("application","octet_stream")
p.set_payload(attachment.read())

# Encode the payload in order to send the binary data in ASCII
encoders.encode_base64(p)
p.add_header("Content-Disposition",f"{attachment}", filename=filename)
msg.attach(p)
# /////////////////////////////////////////////////////////////////////////////////

# enable security
context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com',465,context=context)
server.login(from_email,password)
# Finally the email is ready to be sent
server.sendmail(from_email,to_email,msg.as_string())
print("Email has been sent!")
