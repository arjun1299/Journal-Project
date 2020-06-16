import pyautogui
import subprocess
import os
import cv2
import datetime
import time
import numpy as np


x = datetime.datetime.now()

dirs=os.listdir()

dirName=str(x.date())

if(dirName not in dirs):
    os.mkdir('./'+ dirName)

cap=cv2.VideoCapture(-1)
currentFrame=0;

ret,currentFrame=cap.read()
print(ret)
while ret:
    x = datetime.datetime.now()
    ret,currentFrame=cap.read()

    #if(x.second==0):
    screenshot = pyautogui.screenshot()
    
    screenshot.save(os.getcwd()+'/'+dirName+'/' +str(x.time())+'.png')
    
    screenshot=np.array(screenshot)
    
    print(screenshot.dtype,currentFrame.dtype)
    #print(screenshot.shape[1],currentFrame.shape[1])
    print(screenshot.shape,currentFrame.shape)


    screenshot=cv2.resize(screenshot,(currentFrame.shape[1],currentFrame.shape[0]))
    print(screenshot.shape,currentFrame.shape)

    #np.reshape(screenshot,currentFrame)
    print("captured at" + str(x.time()))
    #screenshot=screenshot.convertTo(dst)
    currentFrame=cv2.vconcat([screenshot,currentFrame])
    cv2.imwrite(os.getcwd()+'/'+dirName+'/' +str(x.time())+'Face'+'.png',currentFrame)

    #time.sleep(50)