from pyrogram import Client
from config import TARGET_ID,API_ID,API_HASH

with open('users.txt', 'r') as f:
    lines = f.read().splitlines()

users = list(map(int,lines))


app = Client("my_account" , api_id=API_ID, api_hash=API_HASH)

with app:
    print("adding.......")
    print(app.add_chat_members(TARGET_ID,users))
