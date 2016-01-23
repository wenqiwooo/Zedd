class CameraController:
	def __init__(self):
		self.id = 1

	def getPicture(self):
		f = open('tmp.jpg', 'rb')
		return f