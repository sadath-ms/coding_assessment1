import smtplib


def send_email(receiver_email, message):
    sender_email = "add here sender email"
    sender_password = "add here sender password"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message)
    print('Email Sent')


if __name__ == '__main__':
    body = input('Body ?')
    recipient = input('Recipient?')
    send_email(recipient, body)




