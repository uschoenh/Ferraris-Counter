from gpiozero import LineSensor
from signal import pause
import time

kwh = 0

counter=0


def zaehler():
    global counter
    counter= counter+1
    print(counter,"x")


def auswerter():
    print(counter,"z")

    
sensor = LineSensor(4)

sensor.when_line = zaehler
sensor.when_no_line = auswerter

print(counter,"y")

if counter==12:
    print("0.1 KWh verbraucht!")
    kwh=+0.1
 



pause()

