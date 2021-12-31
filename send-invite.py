from pyrogram import Client

from config import INVITE_MESSAGE,API_HASH,API_ID

with open('users.txt', 'r') as f:
    lines = f.readlines()

app = Client("my_account",api_id=API_ID, api_hash=API_HASH)

with app:
    for i,line in enumerate(lines):
        user = int(line.strip())
        print("sending")
        app.send_message(user, INVITE_MESSAGE)
        print(i," -Sent to user",user)

