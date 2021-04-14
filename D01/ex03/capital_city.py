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
    
    if city in states:
        cl = states[city]
        cl = cl[0:2]
        if ' ' not in cl:
            print(capital_cities[cl])
    else :
        print('Unknown state')
if __name__ == '__main__':
    if len(argv) > 1:
        capital_city(argv[1])