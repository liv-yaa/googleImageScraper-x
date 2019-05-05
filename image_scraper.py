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
        print('Initialized ImageScraper')


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
        @ return url, a string
        """
        # return 'x'
        term = query[0]
        n = query[1]

        print(term, "...", n)


        # TODO: Generate search url
        # url = "TEMPURL" + term
        
        url = "https://www.google.co.in/search?q=" + term + "&source=lnms&tbm=isch"

        print(url)

        url_n_tuple = (url, n)

        return url_n_tuple




    def get_n_items(self, url_n_tuple):
        """
        @param url_n_tuple - a (string, int) tuple with the url and n 
        @return page - a Response object


        SHOULD ACTUALLY RETURN A HASHMAP OR DATAFRAME

        
        """
        ### TODO - Get my custom URL to pass to download_page, which takes one arg. For now, it's not really working
        # pagex = self.download_page(url_n_tuple[0])
        # print('pagex is', pagex)

        # Returns a response object
        resp = self.download_page('https://www.google.com/search?q=fork&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiQ4oPtkIPiAhUYrZ4KHVmKAygQ_AUIDigB&biw=445&bih=887')
        print('resp', resp)


        # Create a BeautifulSoup object from the Response obejct
        # soup = self.make_soup(resp)
        # print('soup object', soup.prettify())

        # Download images
        self.download_images(resp)


        # Create a hashmap for storing image:metadata
        n_items_hash = {}




        return n_items_hash


    ### HElper function1 for get_n_items ###
    def download_page(self, url_string):
        # Helper function for get_n_items - does it need self?
        # Takes a string
        # Returns a response object or None

        timeout = CONFIG['timeout']
        # print("timeout", timeout)
        try:
            r = requests.get(url_string, timeout=timeout)
            print('r', r)

            return r

        except:
            print("Could not open URL")
            return None


    ### Helper function2 for get_n_items ###
    def download_images(self, response):
        # Does input validation and creates a BeautifulSoup object from Response object
        # Saves them all locally
        # Returns None

        try:
            if response.status_code == 200:

                # Create BS object from the response content
                soup = BeautifulSoup(response.content, 'html.parser')

                # Open images and download them
                imgs = soup.find_all('img')            # Got a hint here for this line: https://stackoverflow.com/questions/35439110/scraping-google-images-with-python3-requests-beautifulsoup                imgs = soup.find_all('div', {'class': 'thumb-pic'})

                for img in imgs:
                    link = img.get('src') 

                    if link:
                        print(link)

                print()



            else:
                print(f'Download page error {page.status_code}')

        except:
            print('Could not get page content')



    ## Final step after get_n_items is download images to local dataframe. Might be a helper function? Not sure
    def download_to_dir(self, hashmap, term):
        """
        @param hashmap has {image:metadata}
        @param term is the search term

        * doesnt return anything *

        Takes a hashmap, creates a file with the search term, and loads all files to it



        """
        return None

    




def main():
    # args = sys.argv
    imgScraper = ImageScraper(args=sys.argv)

    # Process input and do input validation. @return query a list of type [string, int] for keyword, int
    query1 = imgScraper.process_input()
    print('query1', query1, type(query1[0]), type(query1[1])) # list: [<class 'str'>, <class 'int'>]

    url1_tuple = imgScraper.generate_search_url(query1)
    print('url1_tuple', url1_tuple)


    n_images_hashmap = imgScraper.get_n_items(url1_tuple)
    # print('n_images_hashmap', n_images_hashmap)





if __name__ == '__main__':
    main()



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














