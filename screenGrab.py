import pyautogui
import os
from time import sleep
import argparse

import datetime

parser = argparse.ArgumentParser() 

parser.add_argument("-t","--time",default=1,help = "Time interval between pics (default 1 min)") 

mins=parser.parse_args().time

x = datetime.datetime.now()

dirs=os.listdir()

dirName=str(x.date())

if(dirName not in dirs):
    os.mkdir('./'+ dirName)


while 1:
    x = datetime.datetime.now()

    if(x.second==0-1+mins):
        screenshot = pyautogui.screenshot()
        screenshot.save(os.getcwd()+'/'+dirName+'/' +str(x.time())+'.png')
        print("captured at" + str(x.time()))
        sleep(59*t)

