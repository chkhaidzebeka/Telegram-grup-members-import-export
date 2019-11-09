#!/usr/bin/env python3
# -*- encoding: utf-8

# pip3 install telethon

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv

api_id = 11111111       #CHANGE IT WITH YOUR ID
api_hash = 'xxxxxxxxxxxxxxxxx'       # CHANGE IT WITH YOUR HASH
phone = '+xxxxxxxxx'
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('enter reveived code: '))


last_date = None
chunk_size = 200

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))

target_group='group name'       # change it with your grup nick

print('Scrapping Members...')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)

print('Saving In members.csv...')
with open('members.csv', 'w') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['username','first name','last name'])
    for user in all_participants:
        if user.username:
            username= user.username
        else:
            username="ERROR"
        if user.first_name:
            first_name=user.first_name
        else:
            first_name="ERROR"
        if user.last_name:
            last_name=user.last_name
        else:
            last_name="ERROR"
        if user.id:
            user_id=user.id
        else:
            user_id="ERROR"
        print(f'{username},{first_name},{last_name}',file=f)
print('Members scraped successfully.')
