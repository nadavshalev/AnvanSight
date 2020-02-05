#from picamera import PiCamera
#from time import sleep
from proccessing_func import *

imgNum=1
photo_dir = './photos/'
photo_name = 'img' + str(imgNum) + '.jpg'
# camera = PiCamera()

#camera.start_preview()
#sleep(1)
#camera.capture(photo_dir+photo_name)
#camera.stop_preview()

img = pre_proccess(photo_dir+photo_name)
find_sweemerts(img, verbus=False)

#for i in range()
	#imgNum=1
	#photo_name = 'img'+`imgNum`+'.jpg'
	#imgNum += 1

