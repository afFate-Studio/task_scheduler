import smtplib
import pyinputplus as pyip
# TODO finish
# class used to send task list
class Emailer:

    # initializes variables
    def __init__(self, message):
        self.sender = pyip.inputEmail("\nPlease provide the sender gmail address ( ex. sender@gmail.com ): ") # take the users email address
        self.password = pyip.inputPassword("Please provide your gmail app password: ")    # take the users gmail app password
        self.receiver = pyip.inputEmail("Please provide the recievers email address ( ex. reciever@mail.com ): ") # take the email they wish to send the task to
        self.message = message

    # sends email using smtp, requires a sender email, app password, recieving email
    def send_mail(self):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.sender, self.password)
        server.sendmail(self.sender, self.receiver, self.message)
        server.quit()
        