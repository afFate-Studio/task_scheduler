import smtplib
from email.message import EmailMessage
import pyinputplus as pyip

# class used to send task list
class Emailer:

    # initializes variables
    def __init__(self, textfile):
        self.sender = pyip.inputEmail("\nPlease provide the sender gmail address ( ex. sender@gmail.com ): ") # take the users email address
        self.password = pyip.inputPassword("Please provide your gmail app password: ")    # take the users gmail app password
        self.receiver = pyip.inputEmail("Please provide the recievers email address ( ex. reciever@mail.com ): ") # take the email they wish to send the task to
        self.textfile = textfile

    # sends email using smtp, requires a sender email, app password, recieving email
    def send_mail(self):
        # Open the plain text file whose name is in textfile for reading.
        with open(self.textfile) as fp:
            # Create a text/plain message
            msg = EmailMessage()
            msg.set_content(fp.read())

        # me == the sender's email address
        # you == the recipient's email address
        msg['Subject'] = f'The contents of {self.textfile}'
        msg['From'] = self.sender
        msg['To'] = self.receiver

        # Send the message via our own SMTP server.
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(self.sender, self.password)
        s.send_message(msg)
        s.quit()
"""        
        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.sender, self.password)
        server.sendmail(self.sender, self.receiver, self.message)
        server.quit()
        """

        
