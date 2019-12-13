from picamera import PiCamera
from time import sleep

photo_dir = './photos/'
photo_name = 'naama.jpg'
camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture(photo_dir+photo_name)
camera.stop_preview()