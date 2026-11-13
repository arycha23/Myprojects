import turtle as trtl
import math

# Create an empty list of turtles
my_turtles = []

# Use interesting shapes and colors (repeating to get 8 of each)
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

# Create turtle objects with unique shapes and colors
for i in range(6):
    t = trtl.Turtle(shape=turtle_shapes[i])
    t.color(turtle_colors[i])
    t.penup()
    my_turtles.append(t)

# Defines the starting values
startx = 0
starty = 0
angle = 0
side = 100

# Moves the turtle forward
for t in my_turtles:
    t.goto(startx, starty)
    t.setheading(angle)
    t.pendown()
    t.forward(side)
    t.penup()

    startx = t.xcor()
    starty = t.ycor()
    angle -= 45

wn = trtl.Screen()
wn.mainloop()
