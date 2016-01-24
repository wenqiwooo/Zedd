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
from modvoice import Speaker

def handle(msg):
	chat_id = msg['from']['id']

	if 'text' in msg:
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
			lightCtlr.on(4)
			bot.sendMessage(chat_id, 'Setting mood to party...')
		elif command == '/romantic':
			moodCtlr.setMoodRomantic(lightCtlr, mPlayer)
			lightCtlr.on(1)
			bot.sendMessage(chat_id, 'Setting mood to romantic...')
		elif command == '/productive':
			moodCtlr.setMoodProductive(lightCtlr, mPlayer)
			lightCtlr.on(2)
			bot.sendMessage(chat_id, 'Setting mood to productive...')
		elif command == '/glance':
			f = camCtlr.getPicture()
			bot.sendPhoto(chat_id, f)
		elif command == '/speak':
			speaker.say('hello')
			bot.sendMessage(chat_id, 'Speaking...')
		elif command == '/broadcast':
			bot.sendMessage(chat_id, 'Please record your broadcast message...')
		elif command == '/onlight':
			lightCtlr.on(0)
			bot.sendMessage(chat_id, 'Turning on lights...')
		elif command == '/offlight':
			lightCtlr.off()
			bot.sendMessage(chat_id, 'Turning off lights...')
		elif command == '/setBrightness':
			lightCtlr.setBrightness(1)
			bot.sendMessage(chat_id, 'Setting brightness of light...')
		# elif command == '/detect':
  #               f = camCtlr.detectChange()
  #               if f is None:
  #                       bot.sendMessage(chat_id, 'No significant change detected...')
  #               else:
  #                       bot.sendPhoto(chat_id, f)
		elif command == '/whiteLight':
			lightCtlr.on(0)
			bot.sendMessage(chat_id, 'Change to white light...')
		elif command == '/orangeLight':
			lightCtlr.on(1)
			bot.sendMessage(chat_id, 'Change to orange light...')
		elif command == '/coolLight':
			lightCtlr.on(2)
			bot.sendMessage(chat_id, 'Cool lighting...')
		elif command == '/blackLight':
			lightCtlr.on(3)
			bot.sendMessage(chat_id, 'Black lighting')
		elif command == '/brightness1':
			lightCtlr.setBrightness(1)
		elif command == '/brightness2':
			lightCtlr.setBrightness(2)
		elif command == '/brightness3':
			lightCtlr.setBrightness(3)
		elif command == '/brightness4':
			lightCtlr.setBrightness(4)

	elif 'voice' in msg:
		file_id = msg['voice']['file_id']
		bot.downloadFile(file_id, 'voice.ogg')
		mPlayer.broadcast()
		broadcastFlag = 0

# Initialize MusicPlayer
mPlayer = MusicPlayer()

# Initialize LightController
lightCtlr = LightController()

# Initialize MoodController
moodCtlr = MoodController()

# Initialize CameraController
camCtlr = CameraController()

# Initialize Speaker
speaker = Speaker()

# Telegram bot
bot = telepot.Bot('157000180:AAGLth4tTl6T8ZgcfSXmcnDxrlmmC91RG5o')
bot.notifyOnMessage(handle)
print 'Bot listening...'

while 1:
	time.sleep(5)