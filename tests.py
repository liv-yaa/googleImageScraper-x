"""
Olivia Smith 05.04.2019

Integration Tests 


"""
# Do we need to import os?

# Libraries
import unittest
# from unittest.mock import patch
# from unittest import TestCase

from selenium import webdriver


# Local
from image_scraper import ImageScraper




class TestInput(unittest.TestCase):

    def test_process_input(self):
        """
        Tests if process_input() is returning arguments properly

        And that it's catching errors
        """
        print('Testing Input')


        # Returns a list with 2 items?
        input1 = ImageScraper(args=['image_scraper.py', 'dog', 2]).process_input()
        expected1 = ['dog', 2]
        self.assertEqual(input1, expected1)

        # Test exceptions - TODO
        # with self.assertRaises(IndexError) as cm:
        #     input2 = ImageScraper(args=['image_scraper.py', 2]).process_input()
        # err = cm.exception 
        # print('input2 is', input2)
        # print('cm is', cm)
        # print('err is', err)
        # # self.assertEqual(str(err), 'IndexError: list index out of range')


        # expected2 = 'Second argument n_items must be an integer'









class IntegrationTests(unittest.TestCase):
    """
    IntegrationTests class inherits from unittests.TestCase 
    This simulates tests cases by creating a client
    (which tests if GET request was successful)

    """

    def setUp(self):
        self.browser = webdriver.Firefox()
        print(self.browser)

    def tearDown(self):
        self.browser.quit()

    # Everything below does not work

    # def test_title(self, url, title):
    #     self.browser.get("https://www.google.com")
        # self.assertEqual(self.browser.title, title)

    # def test_search_google(self):
    #     self.browser.get(url="https://www.google.com")

    #     x = self.browser.find_element_by_id('gsr')
    #     # x.send_keys("3") 

    #     y = self.browser.find_element_by_id('viewport')
    #     # y.send_keys("4")

    #     print('x', x)
    #     print('y', y)

        # btn = self.browser.find_element_by_id('calc-button')
        # btn.click()

        # result = self.browser.find_element_by_id('result')









if __name__ == "__main__":
    unittest.main()