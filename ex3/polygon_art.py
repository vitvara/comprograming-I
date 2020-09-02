import random
import turtle
def polago(x , y, size, n, clr):
    """
    funtion that draw random polagon and draw in random position 
    by input begin x and y position, size of polagon, number, and collor
    """
    # turtle setting
    turtle.screensize(1000)
    turtle.speed(30)
    turtle.setheading(0)
    turtle.color(clr)
    turtle.fillcolor(clr) 
    turtle.goto(x, y)
    # draw random polagon    
    while n > 1:
        # make random polagon
        turtle.pendown()
        turtle.begin_fill()
        # random size
        s = random.randint(10, size)
        a = random.randint(3, 8)
        for i in range (a):
            turtle.forward(s)
            turtle.left(360 / a)   
        turtle.end_fill()
        n -= 1
        turtle.penup()
        turtle.goto(random.uniform(-300, 300), random.uniform(-300, 300))

    turtle.done

polago(0, 0, 100, 50, "blue")