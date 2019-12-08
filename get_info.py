#!/usr/bin/env python3
# -*- encoding: utf-8

from telethon import TelegramClient,sync
api_id = 111111       #CHANGE IT WITH YOUR ID
api_hash = '111111111'       # CHANGE IT WITH YOUR HASH
phone = '+111111'     # change phone number
session_file='+1111111111.session'        # change with your sessions filename
client = TelegramClient(phone, api_id, api_hash)


client=TelegramClient(session_file,api_id,api_hash) 
client.start()
for chat in client.get_dialogs():
    print(f'CHAT NAME: {chat.name} CHANNEL_ID: {chat.entity.id} ACCESS_HASH: {chat.entity.access_hash}')
