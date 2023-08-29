from car import Car


class Search:
    def __init__(self, search_type):
        self.search_type = search_type
        self.cars = []

    # repr method is a method that allows to return a human readable representation of any data format or an object

    def __repr__(self):
        return "You have searched for {} {} cars".format(len(self.cars), self.search_type)

    def add_car_to_list(self, make, model, year):
        self.cars.append(Car(make, model, year))

    def json(self):
        return dict(search_type=self.search_type, cars=[car.json() for car in self.cars])
