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
        url = "TEMPURL" + term
        # url = 'https://www.google.com/search?q=' + quote(
        #         search_term.encode('utf-8')) + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch' 
        #         + params + '&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'

        print(url)

        url_n_tuple = (url, n)

        return url_n_tuple




    def get_n_items(self, url_n_tuple):
        """
        @param url_n_tuple - a (string, int) tuple with the url and n 
        @return page - a Response object


        SHOULD ACTUALLY RETURN A HASHMAP OR DATAFRAME

        TODO - Threadin?
        """
        timeout = CONFIG['timeout']
        # print("timeout", timeout)

        # Create a hashmap for storing image:metadata
        n_items_hash = {}

        try:
            page = requests.get(url, timeout=timeout)
            print('response', page)

            return page

        except:
            print("Could not open URL")
            # return "Page Not Found"


        return n_items_hash


    ### HElper functions for get_n_items ###

    def search_google(self, query):
        """
        @param query a list of type [string, int]
        @return paths a set of URLS

        TODO - input validation?
        """


        query_name = query[0]
        query_size = query[1]

        print(query_name)
        print(query_size)

        paths = set()

        # for i in range(query_size):
        #     paths.add(f'url {i}')




        return paths

    def get_all_img_tags(self, page):

        # Do input validation if page
        try:
            if page.status_code == 200:
                content = page.content

                # Use BeautifulSoup to parse the content
                soup = BeautifulSoup(content, 'html.parser')
                # print('Soup Prettify', soup.prettify())

                # Create list of BS elements
                tags = list(soup.children)
                print('Soup Children (tags)', tags)
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

                return soup
                print()



            else:
                print(f'Download page error {page.status_code}')

        except:
            print('Could not get page content')



    ## Final step after get_n_items is download images to local dataframe
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
    print('n_images_hashmap', n_images_hashmap)

    # Test download page
    # page1 = imgScraper.download_page("http://dataquestio.github.io/web-scraping-pages/simple.html")
    # print('page1', page1)
    # page2 = imgScraper.download_page("https://www.google.com/search?q=fork&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiQ4oPtkIPiAhUYrZ4KHVmKAygQ_AUIDigB&biw=445&bih=887")
    # print('page2', page2)
    # page3 = imgScraper.download_page('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
    # print('page3', page3)


    # Parse contents from page
    # contents1 = imgScraper.get_all_img_tags(page1)
    # print('contents1', contents1)
    # print()
    # print()
    # contents2 = imgScraper.get_all_img_tags(page2)
    # print('contents2', contents2)
    # contents3 = imgScraper.get_all_img_tags(page3)
    # print('contents3', contents3)



if __name__ == '__main__':
    main()
































