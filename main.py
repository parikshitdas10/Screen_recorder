from PIL import ImageGrab
import numpy as np
import cv2
import datetime
#installed pywin32, gives the resolution of the screen
#from win32api import GETSystemMetrics 

#for getting an unique  and dynamic value to add to the file name
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S') 
file_name = f'{time_stamp}.mp4'

#takes care of the encoding of your video that is required in order to save it
fourcc=cv2.VideoWriter_fourcc('m','p','4','v')  
captured_video = cv2.VideoWriter(file_name,fourcc,20.0,(1680,1050))


#GETSystemMetrics not working, so entered resolution manually
'''
width=GETSystemMetrics(0)
height=GETSystemMetrics(1)
'''


while True:
    img = ImageGrab.grab(bbox=(0,0,1680,1050)) #convert image into a numpy array in order to feed it to opencv
    img_np= np.array(img)
    img_final= cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Screen Capture',img_final)#shows the captured image stored as a numpy array
    captured_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break