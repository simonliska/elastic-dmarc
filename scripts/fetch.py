from imap_tools import MailBox

# get all attachments from INBOX and save them to files
with MailBox('imap.gmail.com').login('YOUR_EMAIL_ADDRESS', 'YOUR_SECRET', 'INBOX') as mailbox:
    for msg in mailbox.fetch('UNSEEN'):
        for att in msg.attachments:
            print(att.filename, att.content_type)
            with open('/var/cache/raw/{}'.format(att.filename), 'wb') as f:
                f.write(att.payload)
