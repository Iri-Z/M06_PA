"""
file: M06.py
author: Iri ZInk
 
July 16th, 2023

purpose: 15.1 Use multiprocessing to create three separate processes. 
Make each one wait a random number of seconds between zero and one,
 print the current time, and then exit.

"""
import multiprocessing
import os
from datetime import datetime
import time
import random

#Randomly picks to wait either 0 or 1 second before printing the process number and the current time
def waitForTime():
    rand = random.randint(0, 1)
    time.sleep(rand)
    now = datetime.today()
    current_time = now.strftime("%H:%M:%S")
    print("Process %s finished at %s" %(os.getpid(), current_time))

#Create the processes and set them to complete the waitForTime function
if __name__ == "__main__":
    
    for n in range(3):
        p = multiprocessing.Process(target=waitForTime)
        p.start()