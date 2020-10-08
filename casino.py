import time, re, sys, asyncio, random
from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession
from os import environ

api_id = environ['id']
api_hash = environ['hash']
string = environ['string1']
client = TelegramClient(StringSession(string), api_id, api_hash)

bot = 'kampungmaifamA2bot'	
async def main():
	async with client:
		while(True):
			num = random.randint(1, 6)
			message = '/casino_Fiftyfifty_{}_5e10'.format(num)
			await client.send_message(bot, message)
			print(message)
			await asyncio.sleep(241)
			await client.send_message(bot, '/casino_result')
			await asyncio.sleep(3)
client.loop.run_until_complete(main())
