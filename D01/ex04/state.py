from sys import argv

def capital_city(city):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if city in list(capital_cities.values):
        position_1 = list(capital_cities.values().index(city))
        position_2 = list(states.values().index(position_1))
        print(position_2)
    else :
        print('Unknown city')

if __name__ == '__main__':
    if len(argv) > 1:
        capital_city(argv[1])