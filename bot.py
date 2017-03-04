import discord
import asyncio
import traceback
import sys
from io import BytesIO, StringIO
import time
import config

client = discord.Client()
VERSION = '0.0.4.'
prefix = config.prefix

@client.event
async def on_ready():
	print('signed in as:')
	print(client.user.name)
	print(client.user.id)
	print('~~~~~~~~~~~')
	print(client)

	

@client.event
async def on_message(message):
	if message.author.id != client.user.id:
		return
	if message.content.startswith('+'):
		print('Command: ' + message.content)
	command = message.content
	parameters = ' '.join(message.content.strip().split(' ')[1:])
	if command.startswith("+shutdown"):
		await reply(message, 'turning off...')
		await client.logout()
	elif command.startswith(prefix + 'time'):
		await reply(message, 'The time and date is: ' + time.ctime())
	elif command.startswith(prefix +'info'):
		await reply(message, 'I am watchbot, a discord selfbot made by Nukekin that tells the time, and I also have other random stuff. I am on version: ' + VERSION + ' I was made in python. I was also inspired by the selfbot [RDT]Test made!! find me at: https://github.com/Steelmaker86/watchselfbot !')
	elif command.startswith(prefix + 'antigrav'):
		await reply(message, 'importing the dopest antigravity memz 35%')
		time.sleep(2)
		await reply(message, 'importing the dopest antigravity memz 69%')
		time.sleep(4)
		await reply(message, 'imported the dopest antigravity memz 420%')
		import antigravity
	elif command.startswith(prefix + 'lenny'):
		await reply(message, '( ͡° ͜ʖ ͡°)')
	elif command.startswith(prefix + 'blank'):
		await reply(message, '')
		##async def reply(message, text):
##	await client.send_message(message.channel, message.author.mention + ', ' + text)

async def reply(message, text):
	await client.edit_message(message, text)

client.run(config.email, config.password)
