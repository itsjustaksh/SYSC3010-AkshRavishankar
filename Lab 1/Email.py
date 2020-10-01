import smtplib

#email vars
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USERNAME = 'raspberripitest@gmail.com'
EMAIL_PASSWORD = 'e.f}AJ7]~(.K'

class Emailer:
    
    def sendEmail(self, recepient, subject, content):
        
        #Create Headers
        headers = ["From: " + EMAIL_USERNAME, "Subject: " + subject, "To: " + recepient, 
                    "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login to gmail 
        session.login(EMAIL_USERNAME,EMAIL_PASSWORD)

        #Send email and Exit
        session.sendmail(EMAIL_USERNAME, recepient, headers + "\r\n\r\n" + content)
        session.quit

sender = Emailer()

sendTo = 'claire.mah@shaw.ca'
emailSubject = "This is Aksh - Check this out"
emailContent = "I sent this from my raspberry pi using python!!!"

sender.sendEmail(sendTo,emailSubject,emailContent)
        