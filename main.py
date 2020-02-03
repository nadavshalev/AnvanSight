from picamera import PiCamera
from time import sleep
imgNum=1
photo_dir = './photos/'
photo_name = 'img'+`imgNum`+'.jpg'
camera = PiCamera()

camera.start_preview()
sleep(1)
camera.capture(photo_dir+photo_name)
camera.stop_preview()


#for i in range()
	#imgNum=1
	#photo_name = 'img'+`imgNum`+'.jpg'
	#imgNum += 1

