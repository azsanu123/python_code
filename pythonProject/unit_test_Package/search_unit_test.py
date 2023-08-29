from unittest import TestCase
from search import Search

class SearchTest(TestCase):
    """unit tests to indicate the search class and its attributes"""

    def test_create_search(self):
        search = Search("used")
        self.assertEqual("used", search.search_type)
        self.assertListEqual([], search.cars)

    def test_repr(self):
        s = Search("used")
        self.assertEqual(s.__repr__())

    def test_single_car_search(self):
        search = Search("used")
        search.add_car_to_list("Audi", "Q7", 2023)
        self.assertEqual(len(search.cars), 1)