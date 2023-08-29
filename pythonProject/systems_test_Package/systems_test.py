from unittest import TestCase
from unittest.mock import patch
from search import Search

import app


class SystemsTest(TestCase):

    def test_print_cars(self):
        search = Search("used")
        search.add_car_to_list("Audi", "Q7", 2023)
        app.searched_cars = {"Test": search}
        with patch("builtins.print") as mocked_print:
            app.print_cars()
            mocked_print.assert_called_with("..You have searched for 1 used cars")

    def test_menu_print_prompts(self):
        with patch("builtins.input") as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.USER_PROMPT)

    def test_menu_call_print_cars(self):
        with patch("app.print_cars") as mocked_print_cars:
            with patch("builtins.input"):
                app.menu()
                mocked_print_cars.assert_called()

    def test_menu_call_print_cars(self):
        with patch("app.print_cars") as mocked_print:
            with patch("builtins.input", return_value="Q"):
                app.menu()
                mocked_print.assert_called()

    def test_create_a_search(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = "used"
            app.create_a_search()
            self.assertIsNotNone(app.searched_cars)

