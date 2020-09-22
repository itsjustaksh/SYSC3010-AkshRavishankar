from sense_hat import SenseHat
import time

"""

    Sense Hat, name initial display


"""


sense = SenseHat()

#color definitions
green = (0,255,0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
nothing = (0,0,0)


def showFirstInitial():
    sense.show_letter("A", back_colour = green)
    time.sleep(1)

def showLastInitial():
    sense.show_letter("R", back_colour = green)
    time.sleep(1)

def turnOff():
    sense.show_letter("", back_colour = nothing)

while True:
    events = sense.stick.get_events()
    for event in events:
        if event.action != "released":
            showFirstInitial()
            showLastInitial()
            turnOff()







