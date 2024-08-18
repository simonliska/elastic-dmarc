# https://pypi.org/project/imap-tools/
from imap_tools import MailBox, OR

EMAIL_ADDRESS = 'YOUR_EMAIL_ADDRESS'
EMAIL_PASSWORD = 'YOUR_SECRET'
LABEL = 'YOUR_LABEL' 

# get all attachments from INBOX and save them to files
with MailBox('imap.gmail.com').login(EMAIL_ADDRESS, EMAIL_PASSWORD, 'INBOX') as mailbox:
    for msg in mailbox.fetch(OR(seen=False, x_gm_label=LABEL)):
        for att in msg.attachments:
            print(att.filename, att.content_type)
            with open('/var/cache/raw/{}'.format(att.filename), 'wb') as f:
                f.write(att.payload)
