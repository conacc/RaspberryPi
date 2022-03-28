# cameraTest
from picamera import PiCamera
from time import sleep
from sense_hat import SenseHat
sense = SenseHat()
camera = PiCamera()

imgNum = 0
w = (255,255,255)
b = (0,0,0)
white = [
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
]
smile = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, w, b, b, w, b, b,
    b, b, b, b, b, b, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, b, b, b, w, b,
    b, w, w, w, w, w, w, b,
    b, b, b, b, b, b, b, b,
]

def take_photo(num):
    camera.start_preview(alpha=200, fullscreen = False, window = (150,150, 640, 480))
    sense.show_letter("5")
    sleep(1)
    sense.show_letter("4")
    sleep(1)
    sense.show_letter("3")
    sleep(1)
    sense.show_letter("2")
    sleep(1)
    sense.show_letter("1")
    sleep(1)
    sense.set_pixels(white)
    sense.set_pixels(smile)
    camera.capture('/home/pi/Desktop/image'+'%d'%(imgNum)+'.png')
    sense.clear()
    camera.stop_preview()

while True:
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            take_photo(imgNum)
            imgNum += 1
        


