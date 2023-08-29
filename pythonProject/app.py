from search import Search

USER_PROMPT = "Enter c to search for a car, p to show previous, s to search for available cars and q to quit: "

searched_cars = dict()

def menu():
    print_cars()
    option = input(USER_PROMPT)

    while option != "Q":
        if option == "C":
            create_a_search()
        elif option == "P":
            print_cars()
        elif option == "S":
            view_previous_searches()
        option = input(USER_PROMPT)

def create_a_search():
    search_type = input("Enter search details: ")
    searched_cars[search_type] = Search(search_type)

def view_previous_searches():
    search_type = input("Enter previous search details: ")
    print_cars(searched_cars[search_type])

def print_cars():
    for key, car in searched_cars.items():
        print("..{}".format(car))