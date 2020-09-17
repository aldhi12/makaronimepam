import time, re, sys, asyncio, random
from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession
from os import environ

api_id = environ['id']
api_hash = environ['hash']
string = environ['string1']
client = TelegramClient(StringSession(string), api_id, api_hash)

bot = 'kampungmaifamx4bot'
mine = '⛏⛏⛏⛏⛏'
eat = '/eat_holysnack'
async def main():
	  async with client:
		  while(True):
			  await client.send_message(bot, eat)
		  	await asyncio.sleep(4)
			  await client.send_message(bot, mine)
		  	await asyncio.sleep(4)
	  		post = await client(GetHistoryRequest(peer=bot,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	  		text = post.messages[0].message
	  		if text.find('Your energy is too low') != -1:
	  			await client.send_message(bot, eat)
	  			await asyncio.sleep(4)
          await client.send_message(bot, eat)
	  			await asyncio.sleep(4)
	  			await client.send_message(bot, mine)
	  			await asyncio.sleep(4)
client.loop.run_until_complete(main())
