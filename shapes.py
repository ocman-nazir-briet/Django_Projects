# # For Triangle

# import the turtle modules 
import turtle 


# define the function
# for triangle
def form_tri(side):
	for i in range(3):
		my_pen.fd(side)
		my_pen.left(120)
		side -= 10

		
# Forming the window screen
tut = turtle.Screen()
tut.bgcolor("green")
tut.title("Turtle")

my_pen = turtle.Turtle()
my_pen.color("orange")

tut = turtle.Screen()		 

# for different shapes
side = 300
for i in range(10):
	form_tri(side)
	side -= 30



# # For Box
# import the turtle modules 
import turtle 

# define the function
# for square
def form_sq(side):
	for i in range(4):
		my_pen.fd(side)
		my_pen.left(90)
		side -= 5

		
# Forming the window screen
tut = turtle.Screen()
tut.bgcolor("green")
tut.title("Turtle")

my_pen = turtle.Turtle()
my_pen.color("orange")

tut = turtle.Screen()		 

# for different shapes
side = 200

for i in range(10):
	form_sq(side)
	side-= 20






# # Hexagon inside Hexagon
# import the turtle modules
import turtle


# define the function
# for hexagon
def form_hex(side):
	for i in range(6):
		my_pen.fd(side)
		my_pen.left(300)
		side -= 2


# Forming the window screen
tut = turtle.Screen()
tut.bgcolor("green")
tut.title("Turtle")

my_pen = turtle.Turtle()
my_pen.color("orange")

tut = turtle.Screen()

# for different sizes
side = 120

for i in range(5):
	form_hex(side)
	side -= 12


# # Turtle Star 
from turtle import *
import turtle as tur
import sys
from time import sleep

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def normal_star(siz, clr, point):
    if point <= 4:
        raise ValueError('Not enough point')

    tur.color(clr)

    for coprime in range(point // 2, 1, -1):
        if gcd(point, coprime) == 1:

            print("({},{})".format(point, coprime), file=sys.stderr)

            start = tur.position()

            for _ in range(point):
                tur.forward(siz)
                tur.left(360.0 / point * coprime)

            tur.setposition(start)

            return

    abnormal_star(siz, clr, point)

def abnormal_star(siz, clr, point):
    
    print("Exception:", point, file=sys.stderr)

for point in range(7, 20):
    tur.reset()
    normal_star(250, 'blue', point)
    sleep(6)

tur.exitonclick()