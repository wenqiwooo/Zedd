import thread
import serial

class LightController:

	def __init__(self):
		self.brightness = 50
		ser = serial.Serial('/dev/ttyS0', 9600)

	def on(self):
		ser.write('')

	def off(self):
		ser.write('')

	def setBrightness(self):
		ser.write('')

	def incBrightness(self):
		ser.write('')

	def decBrightness(self):
		ser.write('')
