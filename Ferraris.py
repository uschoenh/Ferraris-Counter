from gpiozero import LineSensor
from signal import pause
import datetime
import time

kwh = 0

counter=0

def zaehler():
    global counter
    counter= counter+1
    #print(counter,"x")
    if counter==12:
        global kwh
        kwh= kwh + 1
        zeile=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S,"))+str(kwh/10)+"\n"
        #print(zeile)
        f=open(datetime.datetime.now().strftime("%Y-%W")+".csv", 'a+')
        f.write(zeile)
        f.close()
        global counter
        counter=0
 


def auswerter():
    print(counter,"z")

    
sensor = LineSensor(4)

sensor.when_line = zaehler
#sensor.when_no_line = auswerter

#print(counter,"y")

pause()
