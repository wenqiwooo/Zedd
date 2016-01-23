import thread
import serial

class LightController:

	def __init__(self):
		self.brightness = 50
		ser = serial.Serial('COM9', 9600)

	def on(self, mood):
		ans = 100 + mood
		ser.write(ans)

	def off(self):
		ser.write(300)

	def setBrightness(self, brightness):
		ans = 200 + brightness
		ser.write(ans)
