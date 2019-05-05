"""
Olivia Smith 05.04.2019
Coding Challenge for Buzz Software Internship (Vikhyat Chaudhry)

Write a query/program to scrap images from Google Images for the label specified 
and the number of images to be scraped and dowloaded specified.
Inputs: 
1. Label of the type of images to be scraped (example power lines, dogs, cats, etc.)
2. Number of images to be scraped and downloaded onto the local machine

The program should be able to scrap the images and store those images in a folder 
(on our local machine) 
with the name of the label (example if we are scraping images of 'dogs' 
then the label is 'dogs' and hence the folder where all the scraped 
images should be download should also be named 'dogs').

Points would be awarded on coding style, commenting and a documentation of executing the program.


"""
import os
import sys
import requests
from bs4 import BeautifulSoup
from os.path  import basename
from skimage.transform import resize



# Not used yet:
# import grequests #https://github.com/kennethreitz/grequests/blob/master/grequests.py
# import pandas as pd # To create dataframe
# import base64
# import re

# Local config file
from config import CONFIG

class ImageScraper:

    def __init__(self, args):
        """ 
        Create ImageScraper object, set string args to the instance
        """
        self.args = args


    def process_input(self):
        """
        Take a string of command line arguments from user
        @return query a list of type [string, int, url] for keyword, number, and search URL

        """

        while True:

            try:
                arguments = self.args[1:]

                keyword = str(arguments[0])
                n_items = int(arguments[1])


                # Create a custom search url from keyword
                url = self.generate_search_url(keyword)

                query = [keyword, n_items, url]


                return query 

            except IndexError:
                print('Please enter command with 4 args: \
                    \'python3 image_scraper.py \'keyword(s)\' \'number_of_items\'')
                sys.exit(1)

            except ValueError:
                print('Second argument n_items must be an integer')
                sys.exit(1)



    def generate_search_url(self, term):
        """ Generates a URL for a given search term 
        @param query - a list of type [str, int]
        @return url - a str with the search term embedded in the image search URL

        """

        url = "https://www.google.co.in/search?q=" + term + "&source=lnms&tbm=isch"

        return url




    def get_n_items(self, query):
        """
        Download page and download images
        * I chose to use separate functions because timeout could occur *

        @param query - a list of form [term, n, url]
        @return all_items - a set of all image metadata
        
        """
        # parse 
        term = query[0]
        n = query[1]
        url = query[2]


        # Create a response object, using download_page helper function 
        resp = self.download_page(url)

        # Download images from response; Create a nested data structure to store metadata
        all_items = self.download_images(resp, term, n)

        return all_items




    ### HElper function1 for get_n_items ###
    def download_page(self, url_string):
        """
        Create a Response object via streamining; subject to timeout contstraints 

        @param url_string - the url to download from

        @return r - a Response object - or None
        """

        timeout = CONFIG['timeout']

        try:
            # Create a Response object r via streaming and timeout
            r = requests.get(url_string, stream=True, timeout=timeout)

            # Check for successful status code 200
            if r.status_code == 200:
                return r

            else:
                print(f'Download page error {r.status_code}')

        except:
            print("Could not open URL")
            return None


    def download_images(self, response, term, n):
        """
        Parse a Response, create new directory, and add all files to folder.

        @param response - a Response object containing the URL
        @param term p- the search term
        @param n - number of items to return

        @return n_items_set - a set of hashmaps containing file metadata (URL, size, alt text, height, width, and a unique identifier)
        """

        extensions = CONFIG['extensions']

        # Create a hashmap for storing image:metadata
        n_items_set = {}


        # Create directory with term
        if not os.path.exists(term):
            os.mkdir(term)
            print('Successfully made a folder named ', term)

        else:
            print('Folder already exists. ')           
        

        try:

            # Create BS object from the response content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Open images and download them
            img_tags = soup.find_all('img')            # Got a hint here for this line: https://stackoverflow.com/questions/35439110/scraping-google-images-with-python3-requests-beautifulsoup                imgs = soup.find_all('div', {'class': 'thumb-pic'})

            # Set save_path to current directory / new directory
            save_path = os.getcwd() + '/' + term


            for i in range(n):
                img = img_tags[i]
                link = img.get('src') 

                # Create complete name
                completeName = os.path.join(save_path, link + '.jpg')


                if 'http' in link:

                    # https://stackoverflow.com/questions/8024248/telling-python-to-save-a-txt-file-to-a-certain-directory-on-windows-and-mac/8024254
                    with open(os.path.join(save_path, basename(link)), 'wb') as f:

                        f.write(requests.get(link).content)

                        # Check if image needs to be resized
                        size = os.path.getsize(os.path.join(save_path, basename(link)))
                        print('size', size)

                        # Adding metadata https://stackoverflow.com/questions/41183819/python-add-custom-property-metadata-to-file
                        f.fileinfo = {'src' : str(img.get('src')), 
                            'height' : str(img.get('height')), 
                            'width' : str(img.get('width')),
                            'alt' : str(img.get('alt')),
                            'size' : str(size),
                            'id' : i, # Arbitrary readable id
                            }

                        # print('fileinfo',f.fileinfo)


        except:
            print('Could not get page content')


        return n_items_set




def main():
    imgScraper = ImageScraper(args=sys.argv)

    # Get query a list of type [string, int, url] for search term, num items, custom url
    query1 = imgScraper.process_input()

    # Return nested data structure with metadata
    return imgScraper.get_n_items(query1)



if __name__ == '__main__':
    main()



# Hi Vikhyat, here are some 'Trashed' ideas :)

# Create a more readable filename? The name is encrypted :(
# ugly = requests.get(link).content # Ugly filename - should we change?                    
# os.rename(f, 'test' + i + '.jpg')



#     # Trying to decode base64 encryption but Google has a lock!
# def decode(self, string):
#     decoded_string = base64.b64decode(string)
#     print('decoded_string', decoded_string)
#     return decoded_string
    




