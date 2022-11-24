import turtle
import numpy as np


def plotter(h, w, points):
    s = turtle.Screen()
    turtle.screensize(canvwidth=w, canvheight=h, bg=None)
    t = turtle.Turtle()

    max_y = points[:,:,1].max()
    min_y = points[:,:,1].min()
    max_x = points[:,:,0].max()
    min_x = points[:,:,0].min()

    points -= np.array([(min_x+max_x)/2, (min_y+max_y)/2]).reshape(1,1,2)

    for p in points:
        p0, p1 = p
        t.penup()
        t.goto(p0)
        t.pendown()
        t.goto(p1)

    turtle.done()