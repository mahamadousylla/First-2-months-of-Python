print('Mahamadou Sylla 61549479 and Peter Noh 34951962 ICS 31 Lab Asst 4')

print()  # Leaves a blank line.  print('\n') leaves two blank lines.
print()
print('---------- Part (c) ----------')
print()

print('c.1')

def test_number(number, string):
    '''takes as inmput a number
    and string. returns True if
    number has property indicated
    by string'''
    if string == 'even':
        return number % 2 == 0
    if string == 'odd':
        return number % 2 != 0
    if string == 'positive':
        return number > 0
    if string == 'negative':
        return number < 0
    
assert test_number(14, 'even')
assert not test_number(100, 'odd')
assert test_number(33, 'positive')
assert not test_number(100, 'negative')

print(test_number(22, 'even'))
print(test_number(33, 'even'))
print(test_number(44, 'odd'))
print(test_number(1, 'positive'))
print(test_number(-5, 'negative'))
print(test_number(4, 'negative'))
print(not test_number(5, 'positive'))

print('\n')
print('c.2')

def display():
    '''takes zero arguments.
    asks user to input str. prints
    out each word in str'''
    word = str(input('Enter a word:'))
    for w in word:
        print(w)

display()

print('\n')
print('c.3')

def square_list(integers):
    '''takes in list of integers.
    for every number in
    integer square it'''
    for n in integers:
        print(n ** 2)

square_list([4, 5, 6, 7])

print('\n')
print('c.4')

def match_first_letter(one, lists):
    '''takes in one character and a list.
    if item in lists starts with same character as one
    prints item'''    
    for l in lists:
        if l[0] == one:
            print(l)
match_first_letter('B', ['Batman', 'Batman Begins', 'The Dark Knight'])

print('\n')
print('c.5')

def match_area_code(area_codes, phone_numbers):
    '''take in 3digit strings of area
    codes and a list of phone numbers and
    prints digits that have matching area codes'''
    for digits in phone_numbers:
        if digits[0:3] in area_codes:
            print(digits)

match_area_code(['323', '818'], ['3239298019', '8189448798', '8776549832'])

print('\n')
print('c.6')

def match_area_codes(area_codes, phone_numbers):
    '''takes in 3digit strings of area
    codes and a list of phone numbers and returns
    list of digits that match area codes'''
    x = []
    for digits in phone_numbers:
        if digits[0:3] in area_codes:
            x.append(digits)
    return x

print(match_area_codes(['323', '818'], ['3239298019', '8189448798', '8776549832']))


print()  # Leaves a blank line.  print('\n') leaves two blank lines.
print()
print('---------- Part (d) ----------')
print()

print('\n')
print('d.1')

def is_vowel(one_character):
    '''takes one character string
    and returns True if character
    is a vowel'''
    vowel = "a A e E i I o O u U"
    return one_character in vowel
        

assert is_vowel('z') == False
assert is_vowel('i') == True
        
print(is_vowel('c'))
print(is_vowel('a'))
print(is_vowel('o'))
print(is_vowel('U'))
print(is_vowel('e'))

print('\n')
print('d.2')

def print_nonvowels(string):
    '''takes a string and prints
    all characters in string that are
    are not vowels'''
    vowel = "a A e E i I o O u U"
    for s in string:
        if s not in vowel:
            print(s)
        

print_nonvowels('a s e i d f')
print_nonvowels('z t y n i o')

print('\n')
print('d.3')

def nonvowels(one_string):
    '''takes a string and prints
    all characters in string that
    are not vowels'''
    result = ""
    vowel = "a A e E i I o O u U"
    for character in one_string:
        if character not in vowel:
            result = result + character
    return result

assert nonvowels("a e 1 t 3 u s o") == "1t3s"
assert nonvowels("q w e r t # a") == "qwrt#"

print(nonvowels("a e f 5 j k ! b m i"))
print(nonvowels("w e t v c m n o"))


print('\n')    
print('d.4')

def consonants(stringg):
    '''takes a string and
    returns a string with letters
    that are not vowels'''
    vowel = "a A e E i I o O u U"
    x = ""
    for s in stringg:
        if s not in vowel:
            x = x + s
    return x
assert consonants('a b c d e') == 'bcd'
assert consonants('t e w q p') == 'twqp'

print(consonants('qwrfjo'))
print(consonants('asdfjkl'))

print('\n')
print('d.5')

def select_letters(variable, name):
    '''takes in two strings. If first
    string is a v, function returns all vowels
    in second parameter. If first parameter is c
    returns all consonants in second parameter'''
    x = ""
    vowel = "aAeEiIoOuU"
    if variable == 'v':
        for character in name:
            if character in vowel:
                x = x + character
    else:
        if variable == 'c':
            for character in name:
                if character not in vowel:
                    x = x + character
    return x
        
print(select_letters('v', 'abcdefg'))
print(select_letters('c', 'abcdefg'))

print('\n')
print('d.6')

def hide_vowels(a_string):
    '''takes in a string. If letter in the string,
    is a vowel replace letter with a dash'''
    x = ""
    vowel = "a A e E i I o O u U"
    for letter in a_string:
        if letter in vowel:
            a_string = a_string.replace(letter , "-")
    return a_string

print(hide_vowels('abcdefgi'))
print(hide_vowels('I want to go to sleep early today'))

print('\n')

from collections import namedtuple

Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number,
#	best dish, price of that dish

R1 = Restaurant("Taillevent", "French", "343-3434", "Escargots", 24.50)
R2 = Restaurant("La Tour D'Argent", "French", "343-3344", "Ris de Veau", 48.50)
R3 = Restaurant("Pascal", "French", "333-4444", "Bouillabaisse", 32.00)
R4 = Restaurant("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95)
R5 = Restaurant("Thai Dishes", "Thai", "333-4433", "Paht Woon Sen",  8.50)
R6 = Restaurant("Thai Spoon", "Thai", "334-3344", "Mussamun", 9.00)
R7 = Restaurant("McDonald's", "Burgers", "333-4443", "Big Mac", 3.95)
R8 = Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75)
R9 = Restaurant("Wahoo's", "Fish Tacos", "443-4443", "Mahi Mahi Burrito", 7.50)
R10 = Restaurant("In-N-Out Burger", "Burgers", "434-3344", "Cheeseburger", 2.50)
R11 = Restaurant("The Shack", "Burgers", "333-3334", "Hot Link Burger", 4.50)
R12 = Restaurant("Gina's", "Pizza", "334-4433", "Combo Pizza", 12.95)
R13 = Restaurant("Peacock, Room", "Indian", "333-4443", "Rogan Josh", 12.50)
R14 = Restaurant("Gaylord", "Indian", "333-3433", "Tandoori Chicken", 13.50)
R15 = Restaurant("Mr. Chow", "Chinese", "222-3333", "Peking Duck", 24.50)
R16 = Restaurant("Chez Panisse", "California", "222-3322", "Grilled Duck Breast", 25.00)
R17 = Restaurant("Spago", "California", "333-2222", "Striped Bass", 24.50)
R18 = Restaurant("Sriped Bass", "Seafood", "333-2233", "Cedar Plank Salmon", 21.50)
R19 = Restaurant("Golden Pagoda", "Chinese", "232-3232", "Egg Foo Young", 8.50)
R20 = Restaurant("Langer's", "Delicatessen", "333-2223", "Pastrami Sandwich", 11.50)
R21 = Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50)
R22 = Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50)
R23 = Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50)
R24 = Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50)
R25 = Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50)
R26 = Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) 


RL = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16,
	R17, R18, R19, R20, R21, R22, R23, R24, R25, R26]


print()  # Leaves a blank line.  print('\n') leaves two blank lines.
print()
print('---------- Part (e) ----------')
print()

def Restaurant_change_price(restaurant, number):
    '''take in a restaurant object and number. Returns
    restaurant object with same contents as parameter'''
    restaurant = restaurant._replace(price=restaurant.price + number)
    return restaurant

print(Restaurant_change_price(RL[0], 4))

print()  # Leaves a blank line.  print('\n') leaves two blank lines.
print()
print('---------- Part (f) ----------')
print()


print('\n')
print('f.1')
    
def alphabetical(list_of_restaurants):
    '''takes in a list of restaurants
    and sorts the list by name'''
    list_of_restaurants.sort()
    return list_of_restaurants

print(alphabetical(RL))

print('\n')
print('f.2')

def alphabetical_names(list_of_rest):
    '''takes in a list of restaurants
    sorts by the name of each restaurant
    and returns the name of restaurant only'''
    x=[]
    for restaurant in list_of_rest:
        x.append(restaurant.name)
        x.sort()
    return x
print(alphabetical_names(RL))

print('\n')
print('f.3')

def all_Thai(a_list_of_restaurants):
    '''takes in a list of restaurants
    and if restaurants cuisine is Thai,
    return restaurant'''
    x = []
    for restaurant in a_list_of_restaurants:
        if "Thai" in restaurant:
            x.append(restaurant)
    return x
print(all_Thai(RL))

'''This function works too'''
##def all_Thai(a_list_of_restaurants):
##    x = []
##    for restaurant in a_list_of_restaurants:
##        if restaurant.cuisine == "Thai":
##            x.append(restaurant)
##    return x

print('\n')
print('f.4')

def select_cuisine(list_of_rest, str_cuisine):
    '''take in a list of restaurants and a string
    cuisine. Returns a list of all restaurants that
    serve that cuisine'''
    x = []
    for restaurant in list_of_rest:
        if str_cuisine in restaurant:
            x.append(restaurant)
    return x
print(select_cuisine(RL, 'Ethiopian'))
print(select_cuisine(RL, 'Italian'))

print('\n')
print('f.5')

def select_cheaper(list_of_resta, number):
    '''takes in a list of restaurants and a
    float and returns a list of all restaurants
    who price is less than the specified number'''
    x = []
    for restaurant in list_of_resta:
        if restaurant.price < number:
            x.append(restaurant)
    return x
print(select_cheaper(RL, 4.00))
print(select_cheaper(RL, 5.00))

print('\n')
print('f.6')

def average_price(a_list_of_rest):
    '''takes in a list of restaurants
    and returns the average price of
    those restaurants'''
    x = []
    for restaurant in a_list_of_rest:
        x.append(restaurant.price)
        x_average = sum(x) / len(x)
    return x_average
print(average_price(RL))

print('\n')
print('f.7')

print(average_price(select_cuisine(RL, "Indian")))

print('\n')
print('f.8')

print(average_price(select_cuisine(RL, "Chinese") +
                    select_cuisine(RL, "Thai")))

print('\n')
print('f.9') 

print(alphabetical_names(select_cheaper(RL, 15.00)))

print()  # Leaves a blank line.  print('\n') leaves two blank lines.
print()
print('---------- Part (g) ----------')
print()


import tkinter  
my_window = tkinter.Tk() 
my_canvas = tkinter.Canvas(my_window, width=500, height=500)
my_canvas.pack()

def create_rectangle_from_center(x:int,y:int,w:int,h:int):
    my_canvas.create_rectangle(x-(w/2),y-(h/2),x+(w/2),y+(h/2))
create_rectangle_from_center(250,250,300,100)

tkinter.mainloop()    
