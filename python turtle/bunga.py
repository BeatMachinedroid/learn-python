from turtle import *
import colorsys

bgcolor('black')
speed(0)
pensize(3)
hue = 0.0


for i in range(130):
    color = colorsys.hsv_to_rgb(hue,1,1)
    pencolor(color)
    hue += 0.010
    circle(190-i/2,90)
    lt(90)
    circle(190-i/3,90)
    lt(60)

exitonclick()