import random
import time
import datetime
import thread
import telepot
import pygame

# Application specific imports
from modmusic import MusicPlayer

def handle(msg):
	chat_id = msg['from']['id']
	command = msg['text']

	print 'Got message: %s' % command

	if command == '/playmusic':
		mPlayer.play()
		bot.sendMessage(chat_id, 'Playing music...')
	elif command == '/stopmusic':
		mPlayer.stop()
		bot.sendMessage(chat_id, 'Stopping music...')
	elif command == '/pausemusic':
		mPlayer.pause()
		bot.sendMessage(chat_id, 'Pausing song...')
	elif command == '/nextsong':
		mPlayer.next()
		bot.sendMessage(chat_id, 'Playing next song...')

# Initialize MusicPlayer
mPlayer = MusicPlayer()

# Telegram bot
bot = telepot.Bot('157000180:AAGLth4tTl6T8ZgcfSXmcnDxrlmmC91RG5o')
bot.notifyOnMessage(handle)
print 'Bot listening...'

while 1:
	time.sleep(5)