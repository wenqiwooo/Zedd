import thread
import pygame

class MusicPlayer:

	def __init__(self):
		pygame.mixer.init()
		# msg
		# 0: stop
		# 1: play
		# 2: pause
		self.msg = 0
		# stores index of current track playing
		self.playIndex = 0
		self.playList = ['01_-_Maps.ogg', '05_-_Sugar.ogg', '11_-_My_Heart_Is_Open.ogg', '14_-_Lost_Stars.ogg']
		self.size = len(self.playList)

	def play(self):
		if self.msg == 0:
			pygame.mixer.music.load(playList[self.playIndex])
		self.msg = 1
		thread.start_new_thread(self.__playMusic, ())

	def stop(self):
		self.msg = 0
		pygame.mixer.music.stop()

	def pause(self):
		if self.msg == 1:
			pygame.mixer.music.pause()
		self.msg = 2

	def next(self):
		if self.msg != 0:
			pygame.mixer.music.stop()
		self.playIndex = (self.playIndex++) % self.size
		pygame.mixer.music.load(self.playList[self.playIndex])
		self.msg = 1
		thread.start_new_thread(self.__playMusic, ())

	def __playMusic(self):
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			if self.msg != 1:
				break
			continue