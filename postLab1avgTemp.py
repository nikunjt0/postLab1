from sense_hat import SenseHat
from time import sleep
from collections import deque
import matplotlib.pyplot as plt

sense=SenseHat()
d = deque([], maxlen = 500)
avgTemp = []
rawTemp = []
stop = False
while True:
    
    t = sense.get_temperature()
    d.append(t)
    rawTemp.append(t)
    average = sum(d)/len(d)
    
    avgTemp.append(average)
    for event in sense.stick.get_events():
        if event.action =="pressed":
            if event.direction=="middle":
                stop = True
                sense.clear()
                
    if stop:
        break
plt.plot(avgTemp, 'b')
plt.plot(rawTemp, 'r')
plt.show()