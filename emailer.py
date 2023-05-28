import smtplib

# class used to send task list
class Emailer:

    # initializes variables
    def __init__(self, sender, password, reciever, message):
        self.sender = sender
        self.password = password
        self.reciever = reciever
        self.message = message

    # sends email using smtp, requires a sender email, app password, recieving email
    def send_mail(sender, password, receiver, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        server.quit()