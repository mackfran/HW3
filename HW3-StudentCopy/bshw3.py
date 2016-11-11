# Name: Mackenzie Francisco
# uniqname: mackfran
# Section Day/Time: Thursday/1-2PM
# References: Colleen Feola, my HW2 code

# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import urllib.request
from bs4 import BeautifulSoup
import re

# the URL of the website we want to parse
url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
# effectively open and read the url
html = urllib.request.urlopen(url).read()
# decode the HTML text of the website
soup = BeautifulSoup(html, 'lxml')

# convert the html file into a string
string = str(soup)

# replace every occurence of the word "student" with "AMAZING student"
string1 = string.replace('student','AMAZING student')

# replace the main picture with a picture of myself
string2 = string1.replace('https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg', 'Mackenzie.jpeg')

# replace local images with logo provided in media folder
string3 = string2.replace('logo2.png', 'media/logo.png')

# create a new html file and write the contents of the new string to that file
f = open('HW3.html', 'w')
f.write(string3)
f.close()