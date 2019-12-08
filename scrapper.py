#!/usr/bin/env python3
# -*- encoding: utf-8

# pip3 install -r requirements.txt

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv

api_id = 11111111       #CHANGE IT WITH YOUR ID
api_hash = '1111111111111'       # CHANGE IT WITH YOUR HASH
phone = '+11111111111111'     # change phone number
target_group='test'
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('enter reveived code: '))

chats=[]
last_date = None
chunk_size = 200

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue

filename=f'{target_group}.csv'
print(f'Scrapping Members from {target_group}')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)


# user.id   user.access_hash user.username user.first_name user.last_name
print(f'Saving In {filename}...')
with open(filename, 'w') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    for user in all_participants:
        if user.id:
            uid=user.id
        else:
            uid=""

        if user.access_hash:
            uaccess_hash=user.access_hash
        else:
            uaccess_hash=""

        if user.username:
            username=user.username
        else:
            username=""

        if user.first_name:
            first_name=user.first_name
        else:
            first_name=""

        if user.last_name:
            last_name= user.last_name
        else:
            last_name= ""
        print(f'{uid},{username},{first_name},{last_name},{uaccess_hash}',file=f)

print('Members scraped successfully.')
