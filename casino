import time, re, sys, asyncio, random
from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession
from os import environ

api_id = environ['id']
api_hash = environ['hash']
string = environ['string1']
client = TelegramClient(StringSession(string), api_id, api_hash)

bot = 'kampungmaifamx4bot'	
async def main():
	async with client:
		while(True):
			num = random.randint(1, 6)
			message = '/casino_FortuneDice_{}_5e10'.format(num)
			await client.send_message(bot, message)
			print(message)
			
			async for pesan in client.iter_messages(entity=bot, limit=1):
				check = pesan.text
				if 'level increased' in check:
					await client.send_message(bot, message)
					print('Eat')
			await asyncio.sleep(301)
			await client.send_message(bot, '/casino_result')
			await asyncio.sleep(3)
client.loop.run_until_complete(main())
