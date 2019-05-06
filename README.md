## googleImageScraper

#### Description

A query that scrapes images from Google Images for the label specified and the number of images to be scraped and dowloaded specified. Stores them in a local folder with the name of the search query.
Given:
- Label of the type of images to be scraped (example power lines, dogs, cats, etc.)
- Number of images to be scraped and downloaded onto the local machine

#### Setup

- Install requirements:

  ``` pip3 install -r requirements.txt ```

- Run on command line with 2 additional arguments, 'query' and 'n' ex:

  ``` python3 image_scraper.py pug 4 ```


#### Stack, libraries

- Python
- beautifulsoup
- requests
- os
- sys

#### Overview
1. Using sys, command line args are parsed, if valid
2. A search term is generated for google using string formatting with the query name
3. Using Requests, the page is downloaded via a GET request, with a timer configured to halt the process if it takes too long
4. Using os, a new directory with the same name as the query is made in the current directory (if it does not already exist)
5. Using BeautifulSoup, a soup object is created (a list of all html-derived tags) Parsing the BeautifulSoup object allows us to derive just the 'img' tags and any metadata such as alt text
6. Using os, each image is saved in the named directory, along with its corresponding metadata, in a set of hashmaps including 'alt', 'src', 'size', 'id', 'height', and 'width'


