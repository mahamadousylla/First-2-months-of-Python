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
