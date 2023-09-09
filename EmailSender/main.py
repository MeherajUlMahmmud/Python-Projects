from email.message import EmailMessage
import smtplib
import ssl
import sys


FROM_EMAIL = ''
FROM_EMAIL_PASSWORD = ''

SMTP_SERVER = 'smtp.gmail.com'

CONTEXT = ssl.create_default_context()


def send_email(receiver, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = receiver
    
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, 465, context=CONTEXT) as server:
            server.login(FROM_EMAIL, FROM_EMAIL_PASSWORD)
            server.sendmail(FROM_EMAIL, receiver, msg.as_string())
            print('Email sent successfully')
    except Exception as e:
        print('Something went wrong...')
        print(e)


if __name__ == '__main__':

    if len(sys.argv) != 7:
        print("[Usage:] python main.py -r <receiver_email> -s <subject> -b <body>")
        print("[Usage:] python main.py --receiver <receiver_email> --subject <subject> --body <body>")
        print("[Example:] python main.py -r somebody@gmail.com -s 'Hello' -b 'Hello World'")
        sys.exit(1)

    args = {}
    args['receiver'] = sys.argv[2]
    args['subject'] = sys.argv[4]
    args['body'] = sys.argv[6]

    receiver = args['receiver']
    subject = args['subject']
    body = args['body']

    send_email(receiver, subject, body)
