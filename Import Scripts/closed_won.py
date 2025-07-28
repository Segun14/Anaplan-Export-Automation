import tkinter as tk
import threading
import imaplib
import email
from email.header import decode_header
import time
from plyer import notification

should_continue = True

def start_email_checking():
    global should_continue
    should_continue = True
    start_button.config(state="disabled")
    stop_button.config(state="normal")
    threading.Thread(target=email_checking_loop).start()

def stop_email_checking():
    global should_continue
    should_continue = False
    start_button.config(state="normal")
    stop_button.config(state="disabled")

def email_checking_loop():
    global should_continue
    while should_continue:
        # Your email checking code here
        time.sleep(60)

window = tk.Tk()

start_button = tk.Button(window, text="Start", command=start_email_checking)
start_button.pack()

stop_button = tk.Button(window, text="Stop", command=stop_email_checking)
stop_button.pack()

window.mainloop()




email_address = 'closedwonalerts@gmail.com'
email_password = 'frvcyxmcjedifqdu'
imap_server = 'imap.gmail.com'
imap_port = 993  # standard IMAP port
subject_phrase = 'CLOSED BUSINESS'

def login_to_email():
    mail = imaplib.IMAP4_SSL(imap_server, imap_port)
    mail.login(email_address, email_password)
    return mail

def get_unseen_emails_with_subject(mail):
    mail.select('inbox')
    result, data = mail.uid('search', None, f'(UNSEEN SUBJECT "{subject_phrase}")')
    email_ids = data[0].split()
    return email_ids

def send_notification(subject, sender):
    notification.notify(
        title='New Email',
        message=f'Subject: {subject}\nFrom: {sender}',
        timeout=10
    )

def process_emails(mail, email_ids):
    for email_id in email_ids:
        result, message_data = mail.uid('fetch', email_id, '(BODY[HEADER.FIELDS (SUBJECT FROM)])')
        raw_email = message_data[0][1].decode("utf-8")
        email_message = email.message_from_string(raw_email)
        subject = decode_header(email_message["Subject"])[0][0]
        if isinstance(subject, bytes):
            subject = subject.decode()
        sender = decode_header(email_message["From"])[0][0]
        if isinstance(sender, bytes):
            sender = sender.decode()
        send_notification(subject, sender)

def main():
    mail = login_to_email()
    while True:
        try:
            email_ids = get_unseen_emails_with_subject(mail)
            if email_ids:
                process_emails(mail, email_ids)
            time.sleep(60)  # Check for new emails every 60 seconds
        except Exception as e:
            print(f'Error: {e}')
            time.sleep(60)
            mail = login_to_email()

if __name__ == '__main__':
    main()



