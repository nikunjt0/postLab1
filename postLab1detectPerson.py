import time
import datetime
from sense_hat import SenseHat
from time import sleep
from libcamera import controls
import cv2
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import CircularOutput

sense=SenseHat()
picam2=Picamera2()
temp = sense.get_temperature()
humid = sense.get_humidity()
#print(temp, humid)

dispW=1280
dispH=720
picam2.preview_configuration.main.size= (dispW,dispH)
picam2.preview_configuration.main.format= "RGB888"
picam2.preview_configuration.align()
picam2.preview_configuration.controls.FrameRate=30 
picam2.configure("preview")

while True:
    t = sense.get_temperature()
    h = sense.get_humidity()
    #print(t, h)
    if abs(t - temp) > 1: #or abs(h - humid) > 1 : We commented out the humidity due to too much fluctuation
        picam2.start()
        faceCascade=cv2.CascadeClassifier("/home/pi/Documents/lab 1/haarcascade_frontalface_default.xml")
        frame=picam2.capture_array()
        frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(frameGray,1.3,5)
        
        for face in faces:
            x,y,w,h=face
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),3)
        cv2.imshow("Camera Frame", frame)
        time.sleep(0.5)
        key=cv2.waitKey(1) & 0xFF
        
        if key == ord("q"):
            break

cv2.destroyAllWindows()

