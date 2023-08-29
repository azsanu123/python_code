from unittest import TestCase
from search import Search


class SearchIntegrationTest(TestCase):

    def test_single_car_search(self):
        search = Search("used")
        search.add_car_to_list("Audi", "Q7", 2023)
        self.assertEqual(len(search.cars), 1)

    def test_multiple_car_search(self):
        search = Search("used")
        search.add_car_to_list("Audi", "Q7", 2023)
        search.add_car_to_list("Range-Rover", "Sport", 2023)
        search.add_car_to_list("Mercedes", "GLC", 2023)
        self.assertEqual(len(search.cars), 3)
        self.assertEqual(search.__repr__(), "You have searched for 3 used cars")

    def test_json(self):
        search = Search("used")
        search.add_car_to_list("Audi", "Q7", 2023)
        expected = {
            "search_type": "used", "cars": [{"make": "Audi", "model": "Q7", "year": 2023}]
        }
        self.assertDictEqual(expected, search.json())
