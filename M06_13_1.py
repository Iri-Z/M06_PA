"""
file: M06.py
author: Iri ZInk
July 16th, 2023

purpose: #13.1 Write the current date as a string to the text file today.txt.

"""
from datetime import date

#Get the date
currentDate = date.today()

#Create the file
f = open("today.txt", "w")

#Variable for the format of the date
fmt = "%m/%d/%Y"

#Write the date to the created file in the specified format
f.write(currentDate.strftime(fmt))

#Close the file
f.close()
