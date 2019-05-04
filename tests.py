"""
Olivia Smith 05.04.2019

Integration Tests 


"""
# Do we need to import os?

# Libraries
import unittest
# from unittest.mock import patch
# from unittest import TestCase

# Local
import image_scraper




class TestInput(unittest.TestCase):

    def test_process_input(self):
        """
        Tests if process_input() is returning arguments properly

        And that it's catching errors
        """
        print('Testing Input')



        # Returns a list with 2 items?
        # entry1 = ImageScraper()
        # input1 = entry1.process_input('dog 2')
        # expected1 = ['dog', 2]

        # input2 = 'cat 444'
        # expected2 = ['cat', 444]
        # pass









class IntegrationTests(unittest.TestCase):
    """
    IntegrationTests class inherits from unittests.TestCase 
    This simulates tests cases by creating a client
    (which tests if GET request was successful)

    """
    pass



if __name__ == "__main__":
    unittest.main()