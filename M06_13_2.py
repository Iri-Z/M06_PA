"""
file: M06.py
author: Iri ZInk
 
July 16th, 2023

purpose: 13.2 Read the text file today.txt into the string today_string.

"""

#Read the desired file
f = open("today.txt", "r")

#We know there is only one line in the file and can assign it to the desired variable
today_string = f.readline()

#Check the line in case
print(today_string)

#Close the file
f.close()