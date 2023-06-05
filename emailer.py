import smtplib

# class used to send task list
class Emailer:

    # initializes variables
    def __init__(self, sender, password, receiver, message):
        self.sender = sender
        self.password = password
        self.receiver = receiver
        self.message = message

    # sends email using smtp, requires a sender email, app password, recieving email
    def send_mail(self):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.sender, self.password)
        server.sendmail(self.sender, self.receiver, self.message)
        server.quit()
