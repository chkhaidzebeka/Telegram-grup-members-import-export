#!/usr/bin/env python3
# -*- encoding: utf-8
try:
	import sys

	if len(sys.argv) < 2:
		sys.exit(f"USAGE: {sys.argv[0]} INPUT")

	print("[!] importing libraries ...")

	from telethon.sync import TelegramClient
	from telethon.tl.functions.messages import GetDialogsRequest
	from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
	from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
	from telethon.tl.functions.channels import InviteToChannelRequest
	import csv
	import traceback
	import time


	print(f"[!] reading config from {sys.argv[0]} ...")
	api_id = 11111111       #CHANGE IT WITH YOUR ID
	api_hash = '111111111111'       # CHANGE IT WITH YOUR HASH
	phone = '+111111111'
	client = TelegramClient(phone, api_id, api_hash)

	print("[!] trying to connect")
	client.connect()
	if not client.is_user_authorized():
	    client.send_code_request(phone)
	    client.sign_in(phone, input('[?] enter the code: '))

	input_file = sys.argv[1]
	users = []
	print(f"[!] input file {sys.argv[1]} ...")
	print("[!] reading data from input file")
	with open(input_file, encoding='UTF-8') as f:
	    rows = csv.reader(f,delimiter=",",lineterminator="\n")
	    next(rows, None)
	    for row in rows:
	        user = {}
	        user['id'] = int(row[0])
	        user['username'] = row[1]
	        user['access_hash'] = int(row[-1])
	        users.append(user)

	chats = []
	last_date = None
	chunk_size = 200
	groups=[]

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

	target_group='___TARGET___'
	print(f"[!] your group is set as {target_group}")
	channel_id=1111111111			# THIS IS IMPORTANT
	channel_hash=-11111111111111		# THIS IS IMPORTANT

	print(f"\n\t[!] ATTENTION [!]")
	print(f"\t[!] channel id: {channel_id}")
	print(f"\t[!] channel hash: {channel_hash}")
	print("\t[!] CONFIRM THAT INFO IS CORRECT [!]")

	print("\n[!] starting ...")
	target_group_entity = InputPeerChannel(channel_id,channel_hash)


	mode=1

	for user in users:
	    try:
	        print ("Adding {}".format(user['id']))
	        if mode == 1:
	            if user['id'] == "":
	                continue
	            user_to_add = client.get_input_entity(user['id'])
	        else:
	            sys.exit("Invalid Mode Selected. Please Try Again.")
	        client(InviteToChannelRequest(target_group_entity,[user_to_add]))
	        print("Waiting 20 Seconds...")
	        time.sleep(20)
	    except PeerFloodError:
	        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
	    except UserPrivacyRestrictedError:
	        print("The user's privacy settings do not allow you to do this. Skipping.")
	    except:
	        traceback.print_exc()
	        print("Unexpected Error")
	        continue
except KeyboardInterrupt:
	sys.exit("\nProgram closed")
