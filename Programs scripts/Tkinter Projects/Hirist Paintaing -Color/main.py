'''
import colorgram as col

colors = col.extract("200430102527-01-damien-hirst-severed-spots-full-169.jpg", 30)
coloring = []

for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    my_tuple = (r, g, b)
    coloring.append(my_tuple)
    '''
from turtle import Turtle, Screen, colormode
import random

colormode(255)

my_colors = [(198, 12, 32), (250, 237, 17), (39, 76, 189),
             (38, 217, 68),
             (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252),
             (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9),
             (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167),
             (77, 234, 202),
             (52, 234, 243), (3, 67, 40)]

dodo = Turtle()
dodo.penup()
#dodo.hideturtle()

dodo.setheading(120)
dodo.left(90)
dodo.forward(300)
dodo.setheading(0)
numbers_dots = 100

for i in range (1,numbers_dots+1):
    dodo.dot(20,random.choice(my_colors))
    dodo.forward(50)

    if i %10 == 0 :
        dodo.setheading(90)
        dodo.forward(50)
        dodo.setheading(180)
        dodo.forward(500)
        dodo.setheading(0)





'''
for i in range(5):
    for i in range(9):
        dodo.dot(20, random.choice(my_colors))
        dodo.forward(30)
        dodo.dot(20, random.choice(my_colors))

    dodo.left(90)
    dodo.forward(50)
    dodo.left(90)

    for i in range(9):
        dodo.dot(20, random.choice(my_colors))
        dodo.forward(30)
        dodo.dot(20, random.choice(my_colors))

    dodo.right(90)
    dodo.forward(50)
    dodo.right(90)
    
'''


my_screen = Screen()
my_screen.exitonclick()
