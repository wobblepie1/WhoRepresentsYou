
# coding: utf-8

# In[1]:


#The maximum harcoded emails we can handle
#This is arbitrary, but needed, so in the case of an error, you can increase this number
MAX_EMAILS = 200

#the first line contains the user's gmail to send from
#the second contains the secure app password for my 2-factor auth gmail account
#info for this can be found here: https://support.google.com/accounts/answer/185833?hl=en
CREDENTIALS_FILE_NAME = 'credentials.txt'

#Keep the emails as separate lines, one per line
EMAIL_FILE_NAME = 'emails.txt'


# In[2]:


import smtplib
import time
import random


# In[3]:


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# In[4]:


credentialsFile = open(CREDENTIALS_FILE_NAME)
SERVER_USER = credentialsFile.readline().strip()
SERVER_PASSWD = credentialsFile.readline().strip()
credentialsFile.close()


# In[5]:


server = smtplib.SMTP('smtp.gmail.com', 587)


# In[6]:


server.starttls()


# In[7]:


server.login(SERVER_USER, SERVER_PASSWD)


# In[8]:


emailListFile = open(EMAIL_FILE_NAME)
emailList = []


# In[9]:


for X in range(MAX_EMAILS):

    stringChecker = emailListFile.readline().strip()
    if stringChecker is '':
        break
    emailList.append(stringChecker)
    print(emailList[X])
    print(len(emailList))
emailListFile.close()


# In[10]:


print("Loaded " + str(len(emailList)) + " emails from " + EMAIL_FILE_NAME)
for X in emailList:
    print(X)


# In[11]:


for index in range(len(emailList)):
    recipient_email = emailList[index]
    # Create message container - the correct MIME type is multipart/alternative.
    msg = 0
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "An Update on my Senior Project!"
    msg['From'] = SERVER_USER
    msg['To'] = recipient_email

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi everyone!\nHow are you?\nI just sent this email with a script for my senior project at http://www.whorepresentsyou.com!"
    html = """    <html>
        <head></head>
            <body>
                <p>Hi everyone!<br>
                How are you?<br>
                I just sent this email with a script for my senior project at <a href="http://www.whorepresentsyou.com">whorepresentsyou.com!</a>
                </p>
            </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    
    server.sendmail(SERVER_USER, recipient_email, msg.as_string())
    
    print("Sent a message " + " to " + recipient_email + " from " + SERVER_USER + "!")
    if index != (len(emailList) - 1):
            print("All done! No need to wait!")
    else:
        timeDelay = random.randint(30, 120)
        print("Sleeping for " + str(timeDelay) + " seconds (randomized) to prevent spam triggers!")
        time.sleep(timeDelay)


# In[ ]:


server.quit()


# In[27]:


print("Closed connection to email server! Exiting...")

