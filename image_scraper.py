"""
Olivia Smith 05.04.2019
Coding Challenge for Buzz Software Internship (Vikhyat Chaudhry)

Write a query/program to scrap images from Google Images for the label specified 
and the number of images to be scraped and dowloaded specified.
Inputs: 
1. Label of the type of images to be scraped (example power lines, dogs, cats, etc.)
2. Number of images to be scraped and downloaded onto the local machine

The program should be able to scrap the images and store those images in a folder (on our local machine) with the name of the label (example if we are scraping images of 'dogs' then the label is 'dogs' and hence the folder where all the scraped images should be download should also be named 'dogs').

Points would be awarded on coding style, commenting and a documentation of executing the program.


"""
import os
import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd # To create dataframe

class ImageScraper:
    def __init__(self, args):
        self.args = args
        print('Initialized ImageScraper')
        # pass

    def process_input(self):
        """
        Helper function that takes command line arguments from user
        @return arguments a list of arguments

        TODO - input validation?
        """

        while True:

            try:
                arguments = self.args[1:]

                keyword = str(arguments[0])
                n_items = int(arguments[1])

                return [keyword, n_items]

            except IndexError:
                print('Please enter command with 4 args: \
                    \'python3 image_scraper.py \'keyword(s)\' \'number_of_items\'')
                sys.exit(1)

            except ValueError:
                print('Second argument n_items must be an integer')
                sys.exit(1)


            # return False



def main():
    # args = sys.argv
    imgScraper = ImageScraper(args=sys.argv)
    arguments = imgScraper.process_input()

    for arg in arguments:
        print(arg)




if __name__ == '__main__':
    main()
































