# chameleonSpaceJam.py
# @conacc 29/03/2022
from sense_hat import SenseHat
import RPi.GPIO as GPIO  
from time import sleep    # For pausing
GPIO.setmode(GPIO.BCM)    # BCM numbering, not BOARD
GPIO.setup(4, GPIO.IN)    # Sets pin4 to an input


sense = SenseHat()
sense.color.gain = 60 # There are four possible gain values for the colour sensor: 1, 4, 16 and 60
sense.color.integration_cycles = 64

# Set values for white screen
w = (255,255,255)
white_screen = [
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
]
                    
while True:           
    # Turn on white LEDs to reflect light off object
    sense.set_pixels(white_screen)
    
    # Pause to allow user to place object above sensor
    sleep(2 * sense.colour.integration_time)
    
    # Collect RGB data from Colour Sensor
    red, green, blue, clear = sense.colour.colour # readings scaled to 0-256
    print(f"R: {red}, G: {green}, B: {blue}, C: {clear}")
    
    # Set LED to observed colour
    i = (red,green,blue)
    screen = [
                i, i, i, i, i, i, i, i,
                i, i, i, i, i, i, i, i,
                i, i, i, i, i, i, i, i,
                i, i, i, i, i, i, i, i,
                i, i, i, i, i, i, i, i,
                i, i, i, i, i, i, i, i,
                i, i, i, i, i, i, i, i,
                i, i, i, i, i, i, i, i,
            ]  
    sense.set_pixels(screen)
    sleep(7)            
    sense.clear()
