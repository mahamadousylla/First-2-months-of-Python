print("Mahamadou Sylla 61549479 ICS 31 Lab 31 sec 8. Lab Asst 2.")

#Part E(PRICE QUESTION)

#Part C

hours = int(input('How many hours?'))
print('This many hours:', '$',hours)
rate = int(input('How many dollars per hour?'))
print('This many dollars per hour:  ', '$', rate)
print('Weekly salary:  ', '$', hours * rate)

name = str(input('Hello. What is your name?'))
print('Hello,', name)
print("It's nice to meet you.")
age = int(input('How old are you?'))
print('Next year you will be', (age + 1), 'years old.')
print('Good-bye!')

#Part D

krone_per_euro = 7.46
krone_per_british_pound = 10.33
krone_per_dollar = 6.66

print("Please provide this information")
Business_name = str(input("Business name:"))
euros = int(input("Number of euros:"))
british_pound = int(input("Number of pounds:"))
dollar = int(input("Number of dollars:"))
print("Business name:", Business_name)
print(euros, "euros is", euros * krone_per_euro, "krone")
print(british_pound, "pounds is", british_pound * krone_per_british_pound, "krone")
print(dollar, "dollars is", dollar * krone_per_dollar, "krone")

print("Total krone:",(euros*krone_per_euro) + (british_pound*krone_per_british_pound) + (dollar*krone_per_dollar))
                     
                     
###Part E

from collections import namedtuple
Book = namedtuple('Book', 'title author year price')
favorite = Book('Adventures of Sherlock Holmes',
                'Arthur Conan Doyle', 1892, 21.50)
another = Book('Memoirs of Sherlock Holmes', 
               'Arthur Conan Doyle', 1894, 23.50)
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 25.00)

still_another[0]
another[3]
average = ((another[3] + still_another[3] + favorite[3]) / 3)

print(still_another.title)
print(another.price)
print(average)
print(favorite.year < 1900)

still_another = still_another._replace(price=26.00)
print(still_another.price)
still_another = still_another._replace(price=still_another.price *1.2)
print(still_another.price)

#explain why i cant put price on right side of equal sign


#Part F of Lab 2

from collections import namedtuple

Animal = namedtuple('Animal', 'name species age weight favorite_food')
animal_one = Animal("Jumbo", 'elephant', 50, 1000, 'peanuts')
animal_two = Animal("Perry", 'platypus', 7, 1.7, 'shrimp')

print(animal_one)
print(animal_two)
print(animal_one[3] < animal_two[3])

#Part G

booklist = [favorite, another, still_another]

print(booklist[0].price < booklist[1].price)
print(booklist[0].year > booklist[-1].year)

#Part H

Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
#Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]

print(RC[2].name)
print(RC[0].cuisine == RC[3].cuisine)
print(RC[-1].price)

RC.sort()
print(RC)

RC.sort()
print(RC[-1].dish)

RC.sort()
print(RC[0:2])

print(RC[-2:])

RS = []
RS.extend(RC[0:2])
RS.extend(RC[-2:])
print(RS)


#Part I

###1

import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

my_canvas.create_line(100, 100, 300, 100, fill='orange') # Draw orange line
my_canvas.create_line(100, 300, 300, 300, fill='blue')
my_canvas.create_line(100, 100, 100, 300, fill='orange') # Draw orange line
my_canvas.create_line(300, 100, 300, 300, fill='blue')
# Draw blue line

tkinter.mainloop()          # Combine all the elements and display the window


####2

import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

my_canvas.create_line(100, 100, 300, 100, fill='orange') # Draw orange line
my_canvas.create_line(100, 300, 300, 300, fill='blue')
my_canvas.create_line(100, 100, 100, 300, fill='orange') # Draw orange line
my_canvas.create_line(300, 100, 300, 300, fill='blue')
my_canvas.create_line(100, 200, 200, 100, fill='orange') # Draw orange line
my_canvas.create_line(300, 200, 200, 300, fill='blue')
my_canvas.create_line(300, 200, 200, 100, fill='orange') # Draw orange line
my_canvas.create_line(100, 200, 200, 300, fill='blue')
# Draw blue line

tkinter.mainloop()          # Combine all the elements and display the window


####3

import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

my_canvas.create_line(100, 100, 300, 100, fill='orange') # Draw orange line
my_canvas.create_line(100, 300, 300, 300, fill='blue')
my_canvas.create_line(100, 100, 100, 300, fill='orange') # Draw orange line
my_canvas.create_line(300, 100, 300, 300, fill='blue')
my_canvas.create_line(200, 10, 100, 100, fill='orange') # Draw orange line
my_canvas.create_line(200, 10, 300, 100, fill='blue')
my_canvas.create_line(150, 250, 170, 250, fill='green') # Draw orange line
my_canvas.create_line(150, 295, 170, 295, fill='blue')
my_canvas.create_line(150, 250, 150, 295, fill='orange') # Draw orange line
my_canvas.create_line(170, 250, 170, 295, fill='blue')
my_canvas.create_line(250, 150, 275, 150, fill='orange') # Draw orange line
my_canvas.create_line(250, 125, 275, 125, fill='blue')
my_canvas.create_line(250, 150, 250, 125, fill='orange') # Draw orange line
my_canvas.create_line(275, 150, 275, 125, fill='blue')
my_canvas.create_line(250, 140, 275, 140, fill='orange') # Draw orange line
my_canvas.create_line(262, 150, 262, 125, fill='blue')   # Draw blue line

tkinter.mainloop()          # Combine all the elements and display the window

####4


import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

my_canvas.create_oval(100, 100, 300, 200, fill='white') # Draw white
my_canvas.create_oval(160, 100, 250, 200, fill='brown')
my_canvas.create_oval(190, 130, 230, 175, fill='black')




tkinter.mainloop()          # Combine all the elements and display the window

