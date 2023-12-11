from turtle import*
import colorsys
tracer(2)
pensize(2)
speed(0)
h =1
bgcolor("black")
setheading(80)

for i in range(360):
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.008
    fd(i)
    rt(4)
    rt(50)
    fd(200)
    rt(120)
done()