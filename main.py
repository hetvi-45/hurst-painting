import colorgram
import turtle as turtle_module
from turtle import Turtle, Screen
import random
tim = turtle_module.Turtle()
rgb_color = []
colors = colorgram.extract("image.jpg",30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_tuple = (r, g, b)
    rgb_color.append(color_tuple)
print(rgb_color)





turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23), (21, 188, 230), (238, 169, 157), (162, 210, 182), (138, 210, 232), (0, 123, 54), (88, 130, 182), (180, 187, 211)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100
for dot in range(1, num_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if(dot%10 == 0):
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# etch- a scatch project below

def move_forward():
    tim.forward(10)

def move_backward():
    tim.back(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = turtle_module.Screen()
screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")
