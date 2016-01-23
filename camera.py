import picamera 
import time
import os 

from PIL import Image 
from itertools import izip

class Camera: 

	def __init__(self):
		self.camera =picamera.PiCamera()
		self.havePrevPhoto = False 

	def takePhoto(self):
		self.camera.capture('tmp.jpg')

	#return true if there is significant change in photos 
	def detect(self): 
		#capture img1 if i does not alrdy exist 
		if not self.havePrevPhoto: 
			self.camera.capture('img1.jpg')
			time.sleep(10)
			self.havePrevPhoto = True 

		self.camera.capture('img2.jpg')

		# i1 = Image.open('img1.jpg')
		# i2 = Image.open('img2.jpg') 

		# pairs = izip(i1.getdata(), i2.getdata())
		# dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
		# ncomponents = i1.size[0] * i1.size[1] * 3
		# percentageDiff = (dif / 255.0 * 100) / ncomponents
		percentageDiff = self.getPercentageDifference('img1.jpg', 'img2.jpg')
		
		#return whether there was a significant change and replace img1 with img2 
		if percentageDiff > 10: 
			os.remove('img1.jpg')
			os.rename('img2.jpg', 'img1.jpg')
			return True
		else:  
			return False 

	#calculate and return the percentage difference between the 2 images 
	def getPercentageDifferenc(self, img1, img2): 
		i1 = Image.open(img1)
		i2 = Image.open(img2) 

		pairs = izip(i1.getdata(), i2.getdata())
		dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
		print dif 
		ncomponents = i1.size[0] * i1.size[1] * 3
		percentageDiff = (dif / 255.0 * 100) / ncomponents
		return percentageDiff