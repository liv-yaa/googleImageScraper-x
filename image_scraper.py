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

import base64


# import re

# Not used yet:
# import grequests #https://github.com/kennethreitz/grequests/blob/master/grequests.py
# import pandas as pd # To create dataframe

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
        @return query a list of type [string, int] for keyword, int

        """

        while True:

            try:
                arguments = self.args[1:]

                keyword = str(arguments[0])
                n_items = int(arguments[1])


                query = [keyword, n_items]
                return query 

            except IndexError:
                print('Please enter command with 4 args: \
                    \'python3 image_scraper.py \'keyword(s)\' \'number_of_items\'')
                sys.exit(1)

            except ValueError:
                print('Second argument n_items must be an integer')
                sys.exit(1)



    def generate_search_url(self, query):
        """ Generates a URL for a given search term 
        @param query - a list of type [str, int]
        @return url - a str with the search term embedded in the image search URL

        """
        term = query[0]
        # n = query[1]

        # TODO: Generate search url from term of query
        url = "https://www.google.co.in/search?q=" + term + "&source=lnms&tbm=isch"
        print(url)

        return url




    def get_n_items(self, url, term, n):
        """
        Download page and download images
        * I chose to use separate functions because timeout could occur *

        @param url_n_tuple - a (string, int) tuple with the url and n 
        @return all_items - a set of all image metadata
        
        """


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
        @param term p]- the search term
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

                        # Adding metadata https://stackoverflow.com/questions/41183819/python-add-custom-property-metadata-to-file
                        f.fileinfo = {'src' : str(img.get('src')), 
                            'height' : str(img.get('height')), 
                            'width' : str(img.get('width')),
                            'alt' : str(img.get('alt')),
                            'size' : str(os.path.getsize(os.path.join(save_path, basename(link)))),
                            'id' : i, # Arbitrary readable id
                            }

                        print('fileinfo',f.fileinfo)


        except:
            print('Could not get page content')


        return n_items_set




def main():
    # args = sys.argv
    imgScraper = ImageScraper(args=sys.argv)

    # Process input and do input validation. @return query a list of type [string, int] for keyword, int
    query1 = imgScraper.process_input()
    # print('query1', query1, type(query1[0]), type(query1[1])) # list: [<class 'str'>, <class 'int'>]

    url1 = imgScraper.generate_search_url(query1)
    print('url1', url1)

    term = query1[0]
    n = query1[1]

    print('n', n)
    n_images_hashmap = imgScraper.get_n_items(url1, term, n)
    # print('n_images_hashmap', n_images_hashmap)


    # decoded = imgScraper.decode("ANd9GcSrQtf0TW1sRZqoLXvlNDgDE3T92Pf8usC0QrgYD-DJ1UlLo9WMerlg0UWdQg")




if __name__ == '__main__':
    main()



## Final step after get_n_items is download images to local dataframe. Might be a helper function? Not sure
# def download_to_dir(self, hashmap, term):
    #     """
    #     @param hashmap has {image:metadata}
    #     @param term is the search term

    #     * doesnt return anything *

    #     Takes a hashmap, creates a file with the search term, and loads all files to it



    #     """
    #     return None



# This didn't do much

    # def search_google(self, query):
    #     """
    #     @param query a list of type [string, int]
    #     @return paths a set of URLS

    #     TODO - input validation?
    #     """


    #     query_name = query[0]
    #     query_size = query[1]

    #     print(query_name)
    #     print(query_size)

    #     paths = set()

        # for i in range(query_size):
        #     paths.add(f'url {i}')


        # return paths






# Create list of BS elements
# tags = list(soup.children)
# print('Soup Children (tags)', tags)
# print('Type', [type(item) for item in list(soup.children)])

# getting an error when I try to get URL - ?

# html = list(soup.children)[2]
# children = list(html.children)

# print('children', children)

# Pull all text from BodyText div
# artist_name_list = soup.find(class_='img')
# artist_name_list_items = artist_name_list.find_all('a')

# Create for loop to print out all artists' names
# for artist_name in artist_name_list_items:
#     print(artist_name.prettify())





    # Test download page
    # page1 = imgScraper.download_page("http://dataquestio.github.io/web-scraping-pages/simple.html")
    # print('page1', page1)
    # page2 = imgScraper.download_page("https://www.google.com/search?q=fork&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiQ4oPtkIPiAhUYrZ4KHVmKAygQ_AUIDigB&biw=445&bih=887")
    # print('page2', page2)
    # page3 = imgScraper.download_page('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
    # print('page3', page3)




                        # Create a more readable filename? The name is encrypted :(
                        # ugly = requests.get(link).content # Ugly filename - should we change?                    
                        # os.rename(f, 'test' + i + '.jpg')




    # def decode(self, string):
    #     # Trying to decode base64 encryption
    #     decoded_string = base64.b64decode(string)
    #     print('decoded_string', decoded_string)

    #     return decoded_string
    




