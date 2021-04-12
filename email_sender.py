import csv
from email.message import EmailMessage
import smtplib


def get_credentials(filepath):
    email_address = YOUR MAIL
    email_pass = YOUR PASS
    return (email_address, email_pass)


def login(email_address, email_pass, s):
    s.ehlo()
    # start TLS for security
    s.starttls()
    s.ehlo()
    # Authentication
    s.login(email_address, email_pass)
    print("login")


def send_mail():
    s = smtplib.SMTP("smtp.gmail.com", 587)
    email_address, email_pass = get_credentials("./credentials.txt")
    login(email_address, email_pass, s)

    # message to be sent
    subject = "New upcoming updates in our community"
    body = """Hello Technophiles, We are so happy to share a little something regarding our community.
    Our next works include a new role in the community, series of blogs and videos in the most selected technical domains. And finally a Git Hub Organisation
    We will send you the link of the Organisation soon. There are a lot of things you are going to unravel through this community\n
    Regards, Founder"""

    message = EmailMessage()
    message.set_content(body)
    message['Subject'] = subject

    with open("emails.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
        for email in spamreader:
            s.send_message(email_address, email[0], message)
            print("Send To " + email[0])

    # terminating the session
    s.quit()
    print("sent")


if __name__ == "__main__":
    send_mail()
