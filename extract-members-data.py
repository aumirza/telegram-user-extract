from pyrogram import Client
from config import SOURCE_ID ,API_HASH,API_ID

import csv

app = Client("my_account", api_id=API_ID, api_hash=API_HASH)

with app:
    with open("user.csv", 'w', newline='',encoding='utf-8') as file:
        for i,member in enumerate(app.iter_chat_members(SOURCE_ID)):
            writer = csv.writer(file)
            writer.writerow([member.user.id,member.user.username,member.user.first_name,member.user.last_name,member.user.phone_number])
            print("Done",i)
