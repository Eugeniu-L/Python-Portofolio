import smtplib


class Mail:
    def __init__(self):
        self.my_email = "# your email"
        self.my_pass = "# Aplication Key from email configuration"
        self.target = "Target Email"


    def send_email(self, body):

        with smtplib.SMTP("smtp.gmail.com") as connection:

            # ----------------------- SECURE OUR CONNECTION ------------------------------------ #
            connection.starttls()
            # ----------------------- GET CONNECTED TO SERVER ---------------------------------- #
            connection.login(user=self.my_email, password=self.my_pass)
            # ---------------------------- SEND THE EMAIL -------------------------------------- #
            connection.sendmail(from_addr=self.my_email,
                                to_addrs=self.target,
                                msg=f"Subject: Caffe&Work - New Email\n\n{body}")

