from unittest import TestCase
from car import Car

class CarIntegrationTest(TestCase):

    def test_car_mileage(self):
        # creating a car object
        car = Car("Audi", "Q7", 2022)
        current_mileage = car.update_mileage(50000)
        self.assertEqual(current_mileage, car.read_mileage())