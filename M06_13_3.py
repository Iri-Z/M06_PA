"""
file: M06.py
author: Iri ZInk

July 16th, 2023

purpose: 13.3 Parse the date from today_string.

"""
from datetime import datetime
#From last part
f = open("today.txt", "r")
today_string = f.readline()

#Variable for the format of the date
fmt = "%m/%d/%Y"

#13.3 Parse the date from today_string.
today_object = datetime.strptime(today_string, fmt)
print(today_object)

#Close the file
f.close()