import thread
import pygame

class MusicPlayer:

	def __init__(self):
		pygame.mixer.init()
		# msg
		# -1: broadcast
		# 0: stop
		# 1: play
		# 2: pause
		# 3: party
		# 4: romantic
<<<<<<< HEAD
		# 5: productive
=======
		# 5: productivity
>>>>>>> cbf4253d21f39c0e118ca06e52212d7444f98ada
		self.msg = 0
		# stores index of current track playing
		self.playIndex = 0
		self.playList = ['01_-_Maps.ogg', '05_-_Sugar.ogg', '11_-_My_Heart_Is_Open.ogg', '14_-_Lost_Stars.ogg']
		self.partyPlayList = ['Uptown_Funk.ogg']
		self.romanticPlayList = ['Can_You_Feel_The_Love_Tonight.ogg']
<<<<<<< HEAD
		self.productivePlayList = ['10_Emerald_Waters.ogg', '06_Castles_in_the_Air.ogg', '03_Hero_Requiem_.ogg']
=======
		self.productivityPlayList = ['10_Emerald_Waters.ogg', '06_Castles_in_the_Air.ogg', '03_Hero_Requiem_.ogg']
>>>>>>> cbf4253d21f39c0e118ca06e52212d7444f98ada
		self.size = len(self.playList)

	def play(self):
		if self.msg > 2:
			pygame.mixer.music.stop()
			self.msg = 0
		if self.msg == 0:
			pygame.mixer.music.load(self.playList[self.playIndex])
			self.msg = 1
			thread.start_new_thread(self.__playMusic, ())
		elif self.msg == 2:
			self.msg = 1
			thread.start_new_thread(self.__unpauseMusic, ())

	def setMoodParty(self):
		if self.msg != 3:
			self.msg = 3
			pygame.mixer.music.load(self.partyPlayList[0])
			thread.start_new_thread(self.__playMoodMusic, (3, ))

	def setMoodRomantic(self):
		if self.msg != 4:
			self.msg = 4
			pygame.mixer.music.load(self.romanticPlayList[0])
			thread.start_new_thread(self.__playMoodMusic, (4, ))
			
	def setMoodProductivity(self):
		if self.msg != 5:
			self.msg = 5
			pygame.mixer.music.load(self.productivityPlayList[0])
			thread.start_new_thread(self.__playMoodMusic, (5, ))

	def setMoodProductive(self):
		if self.msg != 5:
			self.msg = 5
			pygame.mixer.music.load(self.productivePlayList[0])
			thread.start_new_thread(self.__playMoodMusic, (5, ))

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
		self.playIndex += 1
		self.playIndex = self.playIndex % self.size
		pygame.mixer.music.load(self.playList[self.playIndex])
		self.msg = 1
		thread.start_new_thread(self.__playMusic, ())

	def broadcast(self):
		if self.msg != 1:
			pygame.mixer.music.stop()
			self.msg = -1
		pygame.mixer.music.load('voice.ogg')
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			continue

	def __playMusic(self):
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			if self.msg != 1:
				break
			continue

	def __unpauseMusic(self):
		pygame.mixer.music.unpause()
		while pygame.mixer.music.get_busy() == True:
			if self.msg != 1:
				break
			continue

	def __playMoodMusic(self, identifier):
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			if self.msg != identifier:
				break
			continue
