print('Mahamadou Sylla')

__author__ = 'dgk'

# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2012

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = Collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 n:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 p:  Print all the restaurants
 e:  Remove all restaurants from the list
 c:  Change prices for the dishes served
 f:  Find restaurants at or below certain price
 q:  Quit
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='n':
            r = Restaurant_get_info()
            r=r._replace(menu=Menu_enter(r.menu))
            C = Collection_add(C, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response=='e':
            C=[]
        elif response=='c':
            C = Collection_raise_prices(C)
        elif response=='f':
            Restaurants_certain_prices(C)
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def Restaurant_change_price(C:list):
    '''asks user for percantage change and applies it to price'''
    number = eval(input('Percentage of price increase?:'))
    for restaurant in range(len(C)):
            C[restaurant] = C[restaurant]._replace(price=((number/100) * C[restaurant].price) + C[restaurant].price)
    return C
                  
def Restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Menu:     " + Dishlist_display(self.menu) + "\n\n")

def Dishlist_display(list_of_dishes):
    '''takes in a list of dishes
    and returns one large string of
    each dish followed by a new line'''
    x=""
    for dish in list_of_dishes:
        x = x + str(dish) + '\n'
    return x



def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        [])


#### COLLECTION
# A collection is a list of restaurants

def Collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def Collection_str(C: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_search_by_name(C: list, name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in C:
        if r.name == name:
            result.append(r)
    return result
    # alternative (using a list comprehension):
    # return [r for r in C if r.name == name]

def Collection_add(C: list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C

def Collection_remove_by_name(C: list, name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in C:
        if r.name != name:
            result.append(r)
    return result
    #    Alternative:
    #    return [r for r in self.rests if r.name != name]

#######Dishes

def Dish_str(self):
    return (
        "Dish:     " + self.name + "\n" +
        "Price:    ${:2.2f}".format(self.price) +
        "Calories:     " + self.calories + "\n\n")

def Dish_get_info() -> Restaurant:
    return Dish(
        input("Please enter the dish's name:  "),
        float(input("Please enter the dish price:  ")),
        float(input("Please enter the calories:  ")))

########Menu
Dish = namedtuple('Dish', 'name price calories')

def Menu_enter(menu: list):
    '''asks user to create a new dish and appends it to list of dishes'''
    answer = "" 
    while answer != 'no': #if the user says yes
        answer = input('Would you like to create a new dish? ') #ask user if they want to add
        if answer == 'yes': #if user says yes
            dish = Dish_get_info() #create a new dish
            menu.append(dish) #add that dish to our menu
        else:
            print("answer must be yes or no") #user can only put yes or no

    return menu #return the menu when user says no


def Dish_raise_price(dish):
    '''takes in one dish and increases price
    by specified amount'''
    z=float(input('How much would you like to change price by? '))
    dish = dish._replace(price=((z/100) * dish.price) + dish.price)
    return dish

def Menu_raise_price(menu):
    '''takes in a menu and changes price
    of each dish'''
    result = 0
    for dish in menu:
        menu[result] = Dish_raise_price(dish)
        result += 1
    return menu


def Restaurant_raise_prices(restaurant):
    '''takes in a restaurant and changes menu prices'''
    restaurant = restaurant._replace(menu=Menu_raise_price(restaurant.menu))
    return restaurant


def Collection_raise_prices(list_of_restaurants):
    '''takes in a list of restaurants and returns list
    with dish prices increased by specified amount'''
    for restaurant in list_of_restaurants:
         Restaurant_raise_prices(restaurant)
    return list_of_restaurants

def Restaurants_certain_prices(c):
    x=[]
    z = float(input("Dishes at or below price of: "))
    for restaurant in c:
        for dish in restaurant.menu:
            if dish.price <= z:
                x.append(dish)
    print(x)
    return x
restaurants()


