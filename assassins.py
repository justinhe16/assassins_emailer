import smtplib
from random import shuffle
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# to import my own files that contain secrets (placed in gitignore)
import tokens

MY_ADDRESS = tokens.email_address
PASSWORD = tokens.password

def get_contacts(filename):
  members = []
  with open(filename, mode='r', encoding='utf-8') as contacts_file:
    for contact in contacts_file:
      temp_tuple = (contact.split()[0] + " " + contact.split()[1],contact.split()[2])
      members.append(temp_tuple)
  return members

def read_template(filename):
  with open(filename, 'r', encoding='utf-8') as template_file:
    template_file_content= template_file.read()
  return Template(template_file_content)

def main():
    members = get_contacts('members.txt') 
    message_template = read_template('message.txt')

    # shuffling!
    shuffle(members)

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for index, member in enumerate(members):
      userName = ""
      userNameEmail = ""
      targetName = ""

      userName = member[0]
      userNameEmail = member[1]
      if index == len(members) - 1:
        targetName = members[0][0]
      else:
        targetName = members[index+1][0]

      # just to see pairings in terminal
      print(userName + "(" + userNameEmail + ")" + "-->" + targetName)

      msg = MIMEMultipart()       # create a message

      # add in the actual person name to the message template
      message = message_template.substitute(PERSON_NAME=userName, TARGET_NAME=targetName)

      # setup the parameters of the message
      msg['From']=MY_ADDRESS
      msg['To']=userNameEmail
      msg['Subject']="Your Subject Here"
        
      # add in the message body
      msg.attach(MIMEText(message, 'plain'))
        
      # # send the message via the server set up earlier.
      s.send_message(msg)
      del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()