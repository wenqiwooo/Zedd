import pyttsx
import pyaudio

class Listener:
	def __init__(self):
		self.audio = pyaudio.PyAudio()

class Speaker:
	def __init__(self):
		self.engine = pyttsx.init()
		self.engine.setProperty('rate', 70) # higher rate, speaks faster
		self.voices = self.engine.getProperty('voices')
		self.engine.setProperty('voice', self.voices[2])

	def say(self, msg):
		self.engine.say(msg)
		self.engine.runAndWait()