# 1

import turtle
turtle.speed(10)
turtle.setheading(0)
"""
# define angle
angle_list = [180, 270, 0, 90]
# set list of coller
list_collor = ["yellow", "green", "blue", "red"]
# make 4 hexagon
for i in range(0, 4):
    turtle.goto(0, 0)
    turtle.setheading(angle_list[i])
    turtle.penup()
    turtle.color(list_collor[i])
    turtle.pensize(10)
    turtle.pendown()
    turtle.circle(100, 360, 6)

"""
# 2
"""
# set turtle speed
turtle.speed(10)


# create rectangle that filled
def create_rectangle_fill(size1, size2, start_angle, line_collor, fill_collor):
    turtle.color(line_collor)
    turtle.fillcolor(fill_collor)
    turtle.setheading(start_angle)
    turtle.pendown()
    turtle.begin_fill()
    for i in [1, 2]:
        turtle.forward(size1)
        turtle.right(90)
        turtle.forward(size2)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()


# make sure that pen is up
turtle.penup()
# create background flag
turtle.goto(-200, 100)
create_rectangle_fill(400, 200, 0, "blue", "blue")

# make white cross
turtle.goto(-210, -85)
angle = math.degrees(math.atan(1 / 2))  # find degree that cross the flag
length_ = math.sqrt(400 ** 2 + 200 ** 2)  # find length
create_rectangle_fill(length_ + 10, 40, angle, "white", "white")
turtle.goto(210, -125)
create_rectangle_fill(length_ + 30, 40, 180 - angle, "white", "white")

# make red cross
turtle.goto(-200, -100)
create_rectangle_fill(length_/2 + 10, 13, angle, "red", "red")
turtle.goto(0, 10)
create_rectangle_fill(length_/2 + 10, 13, angle, "red", "red")

turtle.goto(200, -98)
create_rectangle_fill(length_/2 + 10, 13, 180 - angle, "red", "red")
turtle.goto(0, -12)
create_rectangle_fill(length_/2 + 10, 13, 180 - angle, "red", "red")

# make plus white
turtle.goto(-20, -100)
create_rectangle_fill(200, 40, 90, "white", "white")
turtle.goto(-200, 20)
create_rectangle_fill(400, 40, 0, "white", "white")

# make plus red
turtle.goto(-15, -100)
create_rectangle_fill(200, 30, 90, "red", "red")
turtle.goto(-200, 15)
create_rectangle_fill(400, 30, 0, "red", "red")

# delete surplus
turtle.goto(-220, 150)
create_rectangle_fill(440, 50, 0, "white", "white")
turtle.goto(-220, -100)
create_rectangle_fill(440, 50, 0, "white", "white")
turtle.goto(-250, -150)
create_rectangle_fill(440, 50, 90, "white", "white")
turtle.goto(200, -150)
create_rectangle_fill(440, 50, 90, "white", "white")
"""

# 3
"""
turtle.color("yellow")
turtle.fillcolor("yellow")
turtle.penup()
turtle.goto(0, 200)
turtle.begin_fill()
turtle.pendown()
turtle.setheading(-45)
for i in range(1, 5):
    turtle.forward(200)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.pensize(3)
turtle.color("black")
turtle.goto(0, 190)
turtle.pendown()
turtle.setheading(-45)
for i in range(1, 5):
    turtle.forward(185)
    turtle.right(90)
turtle.penup()

turtle.goto(-25, 105)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.forward(50)
turtle.right(90)
turtle.forward(110)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(110)
turtle.end_fill()

turtle.penup()
turtle.color("red")
turtle.fillcolor("red")
turtle.goto(15, 85)
turtle.pendown()
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()

turtle.penup()
turtle.color("green")
turtle.fillcolor("green")
turtle.goto(15, 50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()

turtle.penup()
turtle.color("yellow")
turtle.fillcolor("yellow")
turtle.goto(15, 15)
turtle.pendown()
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
"""

