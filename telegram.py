import random
import time
import datetime
import thread
import telepot
import pygame

# Application specific imports
from modmusic import MusicPlayer
from modlight import LightController
from modmood import MoodController
from modcamera import CameraController

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
	elif command == '/party':
		moodCtlr.setMoodParty(lightCtlr, mPlayer)
		bot.sendMessage(chat_id, 'Setting mood to party...')
	elif command == '/romantic':
		moodCtlr.setMoodRomantic(lightCtlr, mPlayer)
		bot.sendMessage(chat_id, 'Setting mood to romantic...')
	elif command == '/glance':
		f = camCtlr.getPicture()
		bot.sendPhoto(chat_id, f)

# Initialize MusicPlayer
mPlayer = MusicPlayer()

# Initialize LightController
lightCtlr = LightController()

# Initialize MoodController
moodCtlr = MoodController()

# Initialize CameraController
camCtlr = CameraController()

# Telegram bot
bot = telepot.Bot('157000180:AAGLth4tTl6T8ZgcfSXmcnDxrlmmC91RG5o')
bot.notifyOnMessage(handle)
print 'Bot listening...'

while 1:
	time.sleep(5)