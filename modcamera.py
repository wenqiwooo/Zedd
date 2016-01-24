import picamera
import time
import os
import math, operator 

from PIL import Image, ImageChops

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
			time.sleep(1)
			self.havePrevPhoto = True 
		
		self.camera.capture('img2.jpg')
		rmsDiff = self.getRmsDiff('img1.jpg', 'img2.jpg')

		if rmsDiff > 5000: 
			os.remove('img1.jpg')
			os.rename('img2.jpg', 'img1.jpg')
			f = open('img1.jpg','rb')
			return f
		else:  
			return None	

	def getRmsDiff(self, img1, img2):
	    #Calculate the root-mean-square difference between two images

		h1 = Image.open(img1).histogram()
		h2 = Image.open(img2).histogram()

		return math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h1, h2))/len(h1))