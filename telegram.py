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
	elif command == '/productivity':
		moodCtlr.setMoodProductivity(lightCtlr, mPlayer)
		bot.sendMessage(chat_id, 'Setting mood to productivity...')
	elif command == '/glance':
		f = camCtlr.getPicture()
		bot.sendPhoto(chat_id, f)
	elif command == '/detect':
                f = camCtlr.detectChange()
                if f is None:
                        bot.sendMessage(chat_id, 'No significant change detected...')
                else:
                        bot.sendPhoto(chat_id, f)
        elif command == '/whiteLight':
        	lightCtlr.on(0)
	elif command == '/orangeLight':
		lightCtlr.on(1)
	elif command == '/coolLight':
		lightCtlr.on(2)
	elif command == '/blackLight':
		lightCtlr.on(3)
	elif command == '/brightOne':
		lightCtlr.setBrightness(1)
	elif command == '/brightTwo':
		lightCtlr.setBrightness(2)
	elif command == '/brightThree':
		lightCtlr.setBrightness(3)
	elif command == '/brightFour':
		lightCtlr.setBrightness(4)
	elif command == '/help':
		a = 'To turn on light:' + 
		    '/whiteLight to turn on white light' +
		    '/orangeLight to turn on orange light' + 
		    '/coolLight to turn on cool ambience light' +
		    '/blackLight to turn on black light' + ' ' +
		    
		    'To change brightness of light:' +
		    '/brightOne for the the dimmest setting' +
		    '/brightFour for the brightest setting' + ' ' +
		    
		    'Music Commands:' + 
		    '/playmusic to start playng music' + 
		    '/stopmusic to stop playing music' +
		    '/pausemusic to pause the current music' + 
		    '/nextsong to skip the current music' + ' ' + 
		    
		    'Mood Commands:' + 
		    '/productivity to set conducive music and lighting' +
		    '/party to set party lights and music' + 
		    '/romantic to set romantic lights and music'
		    
		bot.sendMessage(chat_id, a)
	
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
