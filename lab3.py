def abbreviate(month):
    return month[0:3]
assert abbreviate('January') == 'Jan'
assert abbreviate('October') == 'Oct'
print(abbreviate('December'))


def find_area_square(number):
    return number**2
assert find_area_square(1) == 1
assert find_area_square(5) == 25
print(find_area_square(8))

import math
def find_area_circle(radius):
    return math.pi * (radius**2)
assert find_area_circle(1) == math.pi
print(find_area_circle(4))
    

def print_even_numbers(integers):
    for n in integers:
        if n % 2 == 0:
            print(n)
print(print_even_numbers([2, 47, 31, 99, 20, 19, 23, 105, 710, 1004]))


def calculate_shipping(number):
    if number < 2:
        return(2.00)
    elif 2 <= number < 10:
        return(5.00)
    elif number >= 10:
        return(5.00 + (number - 10) * 1.5)
    return calculate_shipping
assert calculate_shipping(1) == 2.00
assert calculate_shipping(3) == 5.00
assert calculate_shipping(4.5) == 5.00
print(calculate_shipping(8))
print(calculate_shipping(18))
print(calculate_shipping(2.9))


###################Part D####################

#d.1

def restaurant_price(restaurant):
    return restaurant.price

from collections import namedtuple     # If this line is in your file already, you don't need it again
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]

assert restaurant_price(RC[0]) == 12.50
assert restaurant_price(RC[3]) == 15.50
print(restaurant_price(RC[1]))

##d.2

RC.sort(key=restaurant_price)
print(RC)

##d.3

def costliest(restaurants):
    max_price = 0
    max_price_name = ' '
    for i in restaurants:
        if i.price > max_price:
            max_price = i.price
            max_price_name = i.name
    return(max_price_name)
print(RC)
print(costliest(RC))
        


##d.4

def costliests2(restaurants):
    max_price = 0
    max_price_name = ' '
    for i in restaurants:
        if i.price > max_price:
            max_price = i.price
            max_price_name = i.name
    return(max_price_name)




print()  # Leaves a blank line.  print('\n') leaves two blank lines.
print()
print('---------- Part (e) ----------')
print()

print('e.1')

def book_title(lst):
    '''takes in a list and prints
    each title in the list'''
    for book in lst:
        print(book.title)

from collections import namedtuple

Book = namedtuple('Book', 'author title genre year price instock')

BSI = [
    Book('Orson Scott Card', 'Enders Game', 'Science', 2013, 25.00, 15),
    Book('Lemony Snicket', 'The Beginning','Technology', 1909, 23.00, 21),
    Book('Mark Twain', 'The Reptile Room', 'Technology', 2008, 18.00, 17),
    Book('Lucky Trav', 'The Horoscope', 'Drama', 1999, 14.00, 4),
    Book('Meg Good', 'Delicious', 'Cookbook', 2014, 26.00, 33),
    Book('Chris Paul', 'Sports Illustrated', 'Sports', 2015, 30.00, 50) ]

book_title(BSI)

print('e.2')

def book_order(lists):
    '''takes in a list,
    sorts in alphabetical
    order and prints each title'''
    x=[]
    for i in lists:
        x.append(i.title)
    x.sort()
    for b in x:
        print(b)
book_order(BSI)

print('e.3')

def book_price(listss):
    '''takes in a list
    and increases price by 10%'''
    j = 0
    for i in listss:
        i = i._replace(price=i.price *1.1)
        listss[j] = i
        j = j + 1
    print(listss)
book_price(BSI)


print('e.4')

def book_genres(lsst):
    '''takes in a list.
    If genre is technology, print title'''
    for i in lsst:
        if i.genre == 'Technology':
            print(i.title)
book_genres(BSI)



print('e.5')

def new_list(books):
    '''takes in a list and
    prints title of book if
    released after or before 2000'''

    items_before_2000=[]
    items_after_2000=[]
    for book in books:
    
        if book.year < 2000:
            items_before_2000.append(book.title)

        if book.year > 2000:
            items_after_2000.append(book.title)
    print(items_before_2000)
    print(items_after_2000)
    print("More titles before 2000 is", len(items_before_2000), "vs More titles after 2000 is", len(items_after_2000))

     
        
new_list(BSI)


print('e.6')

def inventory_value(Book):
    '''takes a book and returns
total value inventory of that book'''
    return Book.price * Book.instock
print(inventory_value(BSI[0]))
print(inventory_value(BSI[1]))




def top_value(Book_List):
    '''takes in a list and returns
    book object with highest value inventory'''
    Max_Value = 0
    Saved_Book = ""
    for Book in Book_List:
        Book_Value = Book.price * Book.instock
        if Book_Value > Max_Value:
            Max_Value = Book_Value
            Saved_Book = Book
    return Saved_Book
print(top_value(BSI))
print("The highest-value book is", top_value(BSI).title, "by", top_value(BSI).author, "at a value of $", top_value(BSI).price * top_value(BSI).instock)

