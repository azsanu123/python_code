from unittest import TestCase
from car import Car


class CarUnitTest(TestCase):

    """unit tests to indicate the car model and its attributes"""

    def test_create_car(self):
        # creating a class object
        car = Car("Mercedes", "GLC", 2019)
        # asserting the class object created
        self.assertEqual("Mercedes", car.make)

    def test_car_json(self):
        # creating a car object
        car = Car("Audi", "Q7", 2022)
        expected = dict(make="Audi", model="Q7", year=2022)
        self.assertEqual(expected, car.json())

    def test_get_car_description(self):
        # creating a car object
        car = Car("Audi", "Q7", 2022)
        self.assertEqual("2022 Audi Q7", car.get_car_description())

    def test_car_lighting(self):
        # creating a car object
        car_one = Car("Mitsubishi", "Galant", 2018)
        car_two = Car("Vauxhall", "Astra", 2012)
        car_three = Car("Mini-Cooper", "Mini", 2004)
        self.assertEqual(car_one.check_light_type(), "Your car uses LED lights")
        self.assertEqual(car_two.check_light_type(), "Your car uses XENON lights")
        self.assertEqual(car_three.check_light_type(), "Your car uses HALOGEN lights")

