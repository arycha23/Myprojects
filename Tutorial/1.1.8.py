# a118_turtles_in_traffic.py
# Move turtles horizontally and vertically across screen.
# Stopping turtles when they collide. They change color and back up before stopping.

import turtle as trtl
wn = trtl.Screen()

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

start_y = 50

for i in range(len(shapes)):

    ht = trtl.Turtle(shape=shapes[i])
    ht.penup()
    ht.fillcolor(horiz_colors[i])
    ht.goto(-350, start_y)
    ht.setheading(0)
    horiz_turtles.append(ht)

    vt = trtl.Turtle(shape=shapes[i])
    vt.penup()
    vt.fillcolor(vert_colors[i])
    vt.goto(-start_y, 350)
    vt.setheading(270)
    vert_turtles.append(vt)

    start_y += 50

# check if two turtles collided
def is_collision(t1, t2):
    x1, y1 = t1.position()
    x2, y2 = t2.position()
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return distance < 20

# Track if turtles should stop moving
horiz_stopped = [False] * len(horiz_turtles)
vert_stopped = [False] * len(vert_turtles)

# Move turtles forward one by one
for step in range(100):
    for i in range(len(horiz_turtles)):
        if not horiz_stopped[i]:
            horiz_turtles[i].forward(5)

        if not vert_stopped[i]:
            vert_turtles[i].forward(5)

        # Check for collision
        if not horiz_stopped[i] and not vert_stopped[i]:
            if is_collision(horiz_turtles[i], vert_turtles[i]):

                # Change colors to show collision
                horiz_turtles[i].fillcolor("black")
                vert_turtles[i].fillcolor("black")

                # Back up slightly
                horiz_turtles[i].backward(10)
                vert_turtles[i].backward(10)

                # Stop moving after backing up
                horiz_stopped[i] = True
                vert_stopped[i] = True

wn.mainloop()
