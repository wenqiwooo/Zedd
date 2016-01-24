import thread
import serial

class LightController:

	def __init__(self):
		self.brightness = 50
		self.ser = serial.Serial('/dev/ttyACM1', 9600)

	def on(self, mood):
		if mood == 0:
			self.ser.write('a')
		elif mood == 1:
			self.ser.write('b')
		elif mood == 2:
			self.ser.write('c')
		elif mood == 3:
			self.ser.write('d')
		elif mood == 4:
			self.ser.write('e')

	def off(self):
		self.ser.write('j')

	def setBrightness(self, brightness):
		if brightness == 1:
			self.ser.write('f')
		elif brightness == 2:
			self.ser.write('g')
		elif brightness == 3:
			self.ser.write('h')
		elif brightness == 4:
			self.ser.write('i')