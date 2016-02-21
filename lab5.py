print('Mahamadou Sylla')



print()  # Leaves a blank line.  print('\n') leaves two blank lines.
print()
print('---------- Part (c) ----------')
print()

print('c.1')

from collections import namedtuple

Dish = namedtuple("Dish", "name price calories")

d1 = Dish("Mali", 17.00, 890)
d2 = Dish("Zaire Dishes", 14.00, 760)
d3 = Dish("West African Food", 10.00, 1300)

print('\n')
print('c.2')

def Dish_str(dish):
    '''takes in a dish and
    returns a string in
    specific format'''
    print('{} (${:2f}): {} cal'.format(dish.name, dish.price, dish.calories))
Dish_str(d1)
    
print('\n')
print('c.3')

def Dish_same(dish_1, dish_2):
    '''takes in two dishes and returns
    true if the dish prices and calorie
    count are equal'''
    return dish_1.name == dish_2.name and dish_1.calories == dish_2.calories
assert Dish_same(d1, d2) == False
assert Dish_same(d2, d3) == False
print(Dish_same(d1, d2))
print(Dish_same(d2, d3))

print('\n')
print('c.4')

def Dish_change_price(dish, number):
    '''takes in dish and number returns the dish
    with price increased with that number'''
    dish = dish._replace(price=((number/100) * dish.price) + dish.price)
    return dish
assert Dish_change_price(d3, 100) == Dish(name='West African Food', price=20.00, calories=1300)
print(Dish_change_price(d1, 100))
print(Dish_change_price(d2, -50))
print(Dish_change_price(d3, 50))

print('\n')
print('c.5')

def Dish_is_cheap(dish, number):
    '''takes in a dish and number
    and returns true if dish price
    is less than number'''
    return dish.price < number
assert Dish_is_cheap(d1, 5.00) == False
assert Dish_is_cheap(d2, 4.00) == False
print(Dish_is_cheap(d2, 5))
print(Dish_is_cheap(d3, 20))
        
print('\n')
print('c.6')

DL = [
Dish("Cherokee Specials", 8.00, 510),
Dish("Blackfoot Crab", 9.00, 730),
Dish("West African Favorites", 16.00, 490),
Dish("Philly Cheesesteaks", 14.50, 650),
Dish("Ted's Bulletin", 12.50, 1150)
]
print(DL)
print('\n')
print(len(DL))
print('\n')
DL.sort()
print(DL)
print('\n')
DL.append(Dish("New York Pizza", 5.25, 300))
print(DL)

DL2 = [
Dish("Zaxby's", 11.00, 460),
Dish("Mahamadou's", 24.00, 1400),
Dish("Sylla's", 22.00, 935),
Dish("Bamako Lamb", 33.00, 1250)
]

print('\n')
DL.extend(DL2)
print(DL)
print('\n')

def Dishlist_display(list_of_dishes):
    '''takes in a list of dishes
    and returns one large string of
    each dish followed by a new line'''
    x=""
    for dish in list_of_dishes:
        x = x + str(dish) + '\n'
    print(x)
Dishlist_display(DL)


print('\n')
print('c.7')

def Dishlist_all_cheap(list_of_dishess, number):
    '''takes in a list of dishes and a number
    if every dish price is less than that number
    return true'''
    for dish in list_of_dishess:
        if Dish_is_cheap(dish, number) == False:
            return False
    return True
assert Dishlist_all_cheap(DL2, 4.00) == False
assert Dishlist_all_cheap(DL2, 100.00) == True
print(Dishlist_all_cheap(DL, 11))
print(Dishlist_all_cheap(DL, 2))
print(Dishlist_all_cheap(DL, 35))


print('\n')
print('c.8')

def Dishlist_change_price(list_of_dishes, number):
    '''take in a list of dishes and a number
    representing a percentage change and returns a
    list of dishes with each price changed by the specified
    amount'''
    x=[]
    for dish in list_of_dishes:
        x.append(Dish_change_price(dish, number))
    return x
assert Dishlist_change_price(DL, 50) == [Dish(name='Blackfoot Crab', price=13.5, calories=730), Dish(name='Cherokee Specials', price=12.0, calories=510), Dish(name='Philly Cheesesteaks', price=21.75, calories=650), Dish(name="Ted's Bulletin", price=18.75, calories=1150), Dish(name='West African Favorites', price=24.0, calories=490), Dish(name='New York Pizza', price=7.875, calories=300), Dish(name="Zaxby's", price=16.5, calories=460), Dish(name="Mahamadou's", price=36.0, calories=1400), Dish(name="Sylla's", price=33.0, calories=935), Dish(name='Bamako Lamb', price=49.5, calories=1250)]
print(Dishlist_change_price(DL, 50))
print('\n')
print(Dishlist_change_price(DL, -50))

print('\n')
print('c.9')

def Dishlist_prices(list_of_dishes):
    '''take in a list of dishes and
    returns a list of numbers containing
    just the prices of the dishes'''
    x=[]
    for dish in list_of_dishes:
        x.append(dish.price)
    return x
assert Dishlist_prices(DL2) == [11.0, 24.00, 22.00, 33.00]
print(Dishlist_prices(DL))

print('\n')
print('c.10')

def Dishlist_average(list_of_dishess):
    '''takes in a list of dishes and
    returns the average price of those dishes'''
    return (sum(Dishlist_prices(list_of_dishess)) / len(Dishlist_prices(list_of_dishess)))
assert Dishlist_average(DL2) == 22.5
print(Dishlist_average(DL))


print('\n')
print('c.11')

def Dishlist_keep_cheap(list_of_dishes, number):
    '''takes in a list of dishes and returns a list
    of those dishes on the original list that have prices
    less than that number'''
    x=[]
    for dish in list_of_dishes:
        if dish.price < number:
            x.append(dish)
    return x
assert Dishlist_keep_cheap(DL2, 1.00) ==[]          
assert Dishlist_keep_cheap(DL, 6.00) ==[(Dish("New York Pizza", 5.25, 300))]
print(Dishlist_keep_cheap(DL, 10))
print(Dishlist_keep_cheap(DL, 15))
print(Dishlist_keep_cheap(DL, 25))

print('\n')
print('c.12')

DA = [
Dish("Applejacks", 14.00, 650),
Dish("Red Clams", 7.00, 820),
Dish("Joney's Pizza", 6.50, 400),
Dish("Calvin's Pizzeria", 5.50, 350),
Dish("Togo Beef", 17.00, 680),
Dish("Ghana Crabs", 8.50, 960),
Dish("Burkina Faso Clams", 11.00, 550),
Dish("Chad Steaks", 7.25, 280),
Dish("Kenyan Rice", 16.50, 700),
Dish("Senegal Cafe", 9.50, 350),
Dish("Togo Chicken", 18.00, 680),
Dish("Liberia Lobster", 8.50, 960),
Dish("Honey Oats", 3.00, 240),
Dish("Blue Clams", 6.00, 660),
Dish("Spaghetti", 14.50, 1200),
Dish("Grand Slam", 16.50, 350),
Dish("Omelette", 4.00, 880),
Dish("Zame Rice", 20.50, 1160),
Dish("Plankton", 13.00, 1050),
Dish("Tuna Sandwich", 8.25, 780),
Dish("Carne Asada", 9.50, 730),
Dish("Asada Fries", 10.50, 350),
Dish("Chicken Bowl", 4.75, 500),
Dish("Pollo Bowl", 9.75, 865),
Dish("Barbecue Chicken", 16.90, 1100)
]

def before_and_after():
    '''asks user to input a percentage change
    in price then changes priceby that amount'''
    number = eval(input('Enter percentage change in prices:'))
    Dishlist_display(DA)
    results=0
    for dish in DA:
        DA[results] = dish._replace(price=(((number/100)*dish.price) + dish.price))
        results = results + 1
    Dishlist_display(DA)

before_and_after()


print('\n')
print()  # Leaves a blank line.  print('\n') leaves two blank lines.
print()
print('---------- Part (e) ----------')
print()

print('e.1')

Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])

r3 = Restaurant('Pascal', 'French', '940-752-0107',
                            [Dish('Escargots', 12.95, 250),
                             Dish('Poached Salmon', 18.50, 550),
                             Dish('Rack of Lamb', 24.00, 850),
                             Dish('Marjolaine Cake', 8.50, 950)])
print('\n')
print('e.2')

def Restaurant_first_dish_name(Restaurant):
      '''takes in a restaurant and returns
    the name of the first dish on the restaurant's
    menu'''
      return Restaurant.menu[0].name
assert Restaurant_first_dish_name(r2) == 'Homard Bleu'
print(Restaurant_first_dish_name(r3))

print('\n')
print('e.3')

def Restaurant_is_cheap(restaurant, number):
    '''takes in a restaurant and a number,
    returns true if average price of menu is
    less than number. Otherwise returns false'''
    return Dishlist_average(restaurant.menu) <= number
assert Restaurant_is_cheap(r3, 70) == True
assert Restaurant_is_cheap(r3, 13) == False
print(Restaurant_is_cheap(r3, 60))
print(Restaurant_is_cheap(r3, 16))
print(Restaurant_is_cheap(r3, 15))

##print(Dishlist_average(r3.menu)) Average

print('\n')
print('e.4')


R = [ r1, r2, r3 ]

def Dish_raise_price(dish):
    '''takes in one dish and increases price
    2.50'''
    dish = dish._replace(price=dish.price + 2.50)
    return dish
assert Dish_raise_price(r3.menu[2]) == Dish('Rack of Lamb', 26.50, 850)
print(Dish_raise_price(r1.menu[0]))

print('\n')
def Menu_raise_price(menu):
    '''takes in a menu and changes price
    of each dish'''
    result = 0
    for dish in menu:
        menu[result] = Dish_raise_price(dish)
        result += 1
    return menu
print(Menu_raise_price(r3.menu))

print('\n')
def Restaurant_raise_prices(restaurant):
    '''takes in a restaurant and changes menu prices'''
    restaurant = restaurant._replace(menu=Menu_raise_price(restaurant.menu))
    return restaurant
assert Restaurant_raise_prices(r2) == Restaurant(name='Taillevent', cuisine='French', phone='01-44-95-15-01', menu=[Dish(name='Homard Bleu', price=47.5, calories=750), Dish(name='Tournedos Rossini', price=67.5, calories=950), Dish(name="Selle d'Agneau", price=62.5, calories=850)])
print(Restaurant_raise_prices(r3))

print('\n')
def Collection_raise_prices(list_of_restaurants):
    '''takes in a list of restaurants and returns list
    with dish prices increased 2.50'''
    for restaurant in list_of_restaurants:
         Restaurant_raise_prices(restaurant)
         return list_of_restaurants
assert Collection_raise_prices(R) == [Restaurant(name='Thai Dishes', cuisine='Thai', phone='334-4433', menu=[Dish(name='Mee Krob', price=15.0, calories=500), Dish(name='Larb Gai', price=13.5, calories=450)]), Restaurant(name='Taillevent', cuisine='French', phone='01-44-95-15-01', menu=[Dish(name='Homard Bleu', price=47.5, calories=750), Dish(name='Tournedos Rossini', price=67.5, calories=950), Dish(name="Selle d'Agneau", price=62.5, calories=850)]), Restaurant(name='Pascal', cuisine='French', phone='940-752-0107', menu=[Dish(name='Escargots', price=17.95, calories=250), Dish(name='Poached Salmon', price=23.5, calories=550), Dish(name='Rack of Lamb', price=29.0, calories=850), Dish(name='Marjolaine Cake', price=13.5, calories=950)])]
print(Collection_raise_prices(R))


print('\n')
print('e.5')

def Collection_select_cheap(collection, number):
    '''takes a collection and number and returns
    a list of all restaurants in collection whose
    average price is less than or equal to that number'''
    x=[]
    for restaurant in collection:
        avg_menu_price = 0
        dish_count = 0
        for dish in restaurant.menu:
            avg_menu_price += dish.price
            dish_count += 1
        if avg_menu_price/dish_count <= number:
            x.append(restaurant)
    return x
assert Collection_select_cheap(R, 30) == [Restaurant(name='Thai Dishes', cuisine='Thai', phone='334-4433', menu=[Dish(name='Mee Krob', price=17.5, calories=500), Dish(name='Larb Gai', price=16.0, calories=450)]), Restaurant(name='Pascal', cuisine='French', phone='940-752-0107', menu=[Dish(name='Escargots', price=17.95, calories=250), Dish(name='Poached Salmon', price=23.5, calories=550), Dish(name='Rack of Lamb', price=29.0, calories=850), Dish(name='Marjolaine Cake', price=13.5, calories=950)])]
print(Collection_select_cheap(R, 26))
print('\n')
print(Collection_select_cheap(R, 70))
print('\n')
print(Collection_select_cheap(R, 15))

print('\n')
print()  # Leaves a blank line.  print('\n') leaves two blank lines.
print()
print('---------- Part (g) ----------')
print()

Count = namedtuple('Count', 'letter number')
def letter_count_string(string, vowel):
    '''takes in two parameter. Second parameter
    is a string that specifies which letter to count
    from the single charace from first parameter'''
    a = Count(vowel, string.count(vowel))
    return a
assert letter_count_string('The caaaaabbage', 'a') == Count(letter='a', number=6)
print(letter_count_string('The bagaaaage', 'a'))
print(letter_count_string('I am going to go home and study', 'o'))

print('\n')
def letter_count(string, vowels):
    '''calls the one character count function
    for each vowel being counted and returns a list
    of Counts'''
    x=[]
    for vowel in vowels:
        x.append(letter_count_string(string, vowel))
    return x
assert letter_count('Where are thou', 'eio') == [Count(letter='e', number=3), Count(letter='i', number=0), Count(letter='o', number=1),]
print(letter_count('I have not been home in years. It\s time for me to go now.', 'aeiou'))
print('\n')
print(letter_count('We are already five weeks into this quarter. Time flies.', 'abcd'))
