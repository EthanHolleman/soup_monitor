# Alert system

import smtplib

def connect(sender_address, sender_password, smtp='smtp.gmail.com', port=587):
    smtpobj = smtplib.SMTP(smtp, port)
    smtpobj.starttls()
    smtpobj.login(sender_address, sender_password)
    return smtpobj

def send_message(smtbobj, message, sender_address,
                 reciever_address):
    try:
        smtbobj.sendmail(sender_address, reciever_address, message)
        return 0
    except Exception as e:
        print('Failed to send email')
        print(e)
        return 1


    
    