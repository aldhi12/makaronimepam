import time, asyncio, sys, threading
from telethon import TelegramClient, events, utils
from telethon.tl.functions.messages import GetHistoryRequest
from os import environ
from telethon.sessions import StringSession

api_id = environ['id']
api_hash = environ['hash']
string = environ['string1']
client = TelegramClient(StringSession(string), api_id, api_hash)


bot = 'kampungmaifamx4bot'
cook = '/cook_minibacon_300'
levelup = '/levelupGuild'
restore = '/eat_holysnack'

async def main():
	async with client:
		while(True):
			await client.send_message(bot, cook)
			await asyncio.sleep(3)
			post = await client(GetHistoryRequest(peer=bot,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
			text = post.messages[0].message
			if text.find('Your energy is too low') != -1:
				await client.send_message(bot, restore)
				await asyncio.sleep(3)
        			await client.send_message(bot, restore)
				await asyncio.sleep(3)
				await client.send_message(bot, cook)
				await asyncio.sleep(3)
			elif text.find('Not enough material') != -1:
				break
			await client.send_message(bot, levelup)
			await asyncio.sleep(60)
client.loop.run_until_complete(main())
