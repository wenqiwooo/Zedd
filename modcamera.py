import picamera
import time
import os

from PIL import Image
from itertools import izip 

class CameraController:
	def __init__(self):
		self.camera =picamera.PiCamera()
		self.havePrevPhoto = False 

	def getPicture(self):
                self.camera.capture('tmp.jpg')
		f = open('tmp.jpg', 'rb')
		return f

        def detectChange(self):
                if not self.havePrevPhoto: 
			self.camera.capture('img1.jpg')
			time.sleep(10)
			self.havePrevPhoto = True 

		self.camera.capture('img2.jpg')
                percentageDiff = self.getPercentageDifference('img1.jpg', 'img2.jpg')

                if percentageDiff > 10: 
			os.remove('img1.jpg')
			os.rename('img2.jpg', 'img1.jpg')
			f = open('img1.jpg','rb')
			return f
		else:  
			return None	

	def getPercentageDifferenc(self, img1, img2): 
		i1 = Image.open(img1)
		i2 = Image.open(img2) 

		pairs = izip(i1.getdata(), i2.getdata())
		dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
		print dif 
		ncomponents = i1.size[0] * i1.size[1] * 3
		percentageDiff = (dif / 255.0 * 100) / ncomponents
		return percentageDiff
