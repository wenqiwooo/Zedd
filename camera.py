import picamera 
import time
import os 

from PIL import Image 
from itertools import izip

class Camera: 

	def __init__(self):
		self.camera =picamera.PiCamera(); 
		self.havePrevPhoto = False 

	def takePhoto(self):
		self.camera.capture('tmp.jpg')

	def detect(self): 
		if not havePrevPhoto: 
			self.camera.capture('img1.jpg')
			time.sleep(10)
			self.havePrevPhoto = True 
		self.camera.capture('img2.jpg')
		percentageDiff = getPercentageDifference(img1.jpg, img2.jpg)
		if percentageDiff > 20: 
			os.rename('img2.jpg', 'tmp.jpg')
			return True
		else 
			return False 

	def getPercentageDifferenc(img1, img2): 
		i1 = Image.open(img1)
		i2 = Image.open(img2) 

		pairs = izip(i1.getdata(), i2.getdata())
		dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
		ncomponents = i1.size[0] * i1.size[1] * 3
		percentageDiff = (dif / 255.0 * 100) / ncomponents
		return percentageDiff


