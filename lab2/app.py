from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import smtplib
import ssl
import imaplib
import email


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/mail', methods=['GET', 'POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        MailOperations(post_data.get('password'), post_data.get('email')).send_email(post_data.get('subject'),
                                                                                     post_data.get('message'),
                                                                                     post_data.get('receiver'))
        response_object['message'] = 'Message sent!'
    else:
        mails = MailOperations(request.args['password'], request.args['email']).readMail()
        return jsonify({
            'status': 'success',
            'mails': mails
        })
    return jsonify(response_object)

class MailOperations:
    def __init__(self, password, email):
        self.portSSL = 465
        self.smtp_server = "smtp.gmail.com"
        self.sender_email = email
        self.password = password

    def send_email(self, subject, text, receiver_email):
        message = """\
Subject: {}

{}""".format(subject, text)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.portSSL, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, receiver_email, message)

    def readMail(self):
        EMAIL = self.sender_email
        PASSWORD = self.password
        SERVER = 'imap.gmail.com'
        x = []

        # connect to the server and go to its inbox
        mail = imaplib.IMAP4_SSL(SERVER)
        mail.login(EMAIL, PASSWORD)
        # we choose the inbox but you can select others
        mail.select('inbox')

        # we'll search using the ALL criteria to retrieve
        # every message inside the inbox
        # it will return with its status and a list of ids
        status, data = mail.search(None, 'ALL')
        # the list returned is a list of bytes separated
        # by white spaces on this format: [b'1 2 3', b'4 5 6']
        # so, to separate it first we create an empty list
        mail_ids = []
        # then we go through the list splitting its blocks
        # of bytes and appending to the mail_ids list
        for block in data:
            # the split function called without parameter
            # transforms the text or bytes into a list using
            # as separator the white spaces:
            # b'1 2 3'.split() => [b'1', b'2', b'3']
            mail_ids += block.split()

        # now for every id we'll fetch the email
        # to extract its content
        for i in mail_ids:
            # the fetch function fetch the email given its id
            # and format that you want the message to be
            status, data = mail.fetch(i, '(RFC822)')

            # the content data at the '(RFC822)' format comes on
            # a list with a tuple with header, content, and the closing
            # byte b')'
            for response_part in data:
                # so if its a tuple...
                if isinstance(response_part, tuple):
                    # we go for the content at its second element
                    # skipping the header at the first and the closing
                    # at the third
                    message = email.message_from_bytes(response_part[1])

                    # with the content we can extract the info about
                    # who sent the message and its subject
                    mail_from = message['from']
                    mail_subject = message['subject']

                    # then for the text we have a little more work to do
                    # because it can be in plain text or multipart
                    # if its not plain text we need to separate the message
                    # from its annexes to get the text
                    if message.is_multipart():
                        mail_content = ''

                        # on multipart we have the text message and
                        # another things like annex, and html version
                        # of the message, in that case we loop through
                        # the email payload
                        for part in message.get_payload():
                            # if the content type is text/plain
                            # we extract it
                            if part.get_content_type() == 'text/plain':
                                mail_content += part.get_payload()
                    else:
                        # if the message isn't multipart, just extract it
                        mail_content = message.get_payload()

                    # and then let's show its result
                    y = {"from": mail_from,
                         "subject": mail_subject,
                         "content": mail_content
                         }
                    x.append(y)
        return x


if __name__ == '__main__':
    app.run()