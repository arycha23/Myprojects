
#   a114_nested_loops_4.py
import turtle as trtl

painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()
move_x = 1
move_y = 1

x = -200
y = 0
while (x<1):
    while (y < 100):
        x = x + move_x
        y = y + move_y
        painter.goto(x,y)
    move_y = -1

    while (y > 0):
        x = x + move_x
        y = y + move_y
        painter.goto(x,y)
    move_y = 1
while (y < 1):
    while (x > 100):
        x = x - move_x
        y = y - move_y
        painter.goto(x,y)
    move_y = 1

    while (x > 0):
        x = x - move_x
        y = y + move_y
        painter.goto(x,y)
    move_y = -1

# For Negative Quadrant
    while (x > -100):
        x = x - move_x
        y = y + move_y
        painter.goto(x,y)
    move_y = 1

    while (x != -200):
        x = x - move_x
        y = y + move_y
        painter.goto(x,y)
    move_y = 1

wn = trtl.Screen()
wn.mainloop()
