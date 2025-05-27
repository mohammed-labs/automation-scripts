
import imaplib
import email
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets auth
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('your-creds.json', scope)
sheet = gspread.authorize(creds).open('Email Log').sheet1

# Email login
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('your_email@gmail.com', 'your_password')
mail.select('inbox')

# Fetch emails
_, data = mail.search(None, 'UNSEEN')
email_ids = data[0].split()

for e_id in email_ids:
    _, msg_data = mail.fetch(e_id, '(RFC822)')
    msg = email.message_from_bytes(msg_data[0][1])
    subject = msg['subject']
    sender = msg['from']
    sheet.append_row([sender, subject])
