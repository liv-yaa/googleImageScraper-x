"""
Olivia Smith 05.04.2019
Coding Challenge for Buzz Software Internship (Vikhyat Chaudhry)

Write a query/program to scrap images from Google Images for the label specified and the number of images to be scraped and dowloaded specified.
Inputs: 
1. Label of the type of images to be scraped (example power lines, dogs, cats, etc.)
2. Number of images to be scraped and downloaded onto the local machine

The program should be able to scrap the images and store those images in a folder (on our local machine) with the name of the label (example if we are scraping images of 'dogs' then the label is 'dogs' and hence the folder where all the scraped images should be download should also be named 'dogs').

Points would be awarded on coding style, commenting and a documentation of executing the program.


"""

import requests
