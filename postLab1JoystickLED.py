from sense_hat import SenseHat
from time import sleep

sense=SenseHat()
blue= (0,0,255)
yellow= (255,255,0)
sense.set_pixel(2, 4, (255, 255, 255))
x = 2
y = 4
stop = False
while True:
    for event in sense.stick.get_events():
        
        print(event.direction,event.action)
        
        if event.action =="pressed":  ## check if the joystick was pressed
            sense.clear()
            if event.direction=="right":   ## to check for other directions use "up", "down", "left", "right"
                x+=1
                if(x > 7):
                    x = 7
            elif event.direction=="left":
                x-=1
                if(x<0):
                    x=0
            elif event.direction=="up":
                y-=1
                if(y<0):
                    y=0
            elif event.direction=="down":
                y+=1
                if(y>7):
                    y=7
            elif event.direction=="middle":
                stop = True
                sense.clear()
        if stop:
            break
        
    
    sense.set_pixel(x, y, (255, 255, 255))            
          
          
          

