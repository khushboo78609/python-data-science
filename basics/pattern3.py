from turtle import *

speed('slowest')
pensize(2)
penup()
goto(-500,0)
pendown()
lt(60)


for i in range(10):
    fd(120)
    rt(100)
    fd(120)
    lt(100)
hideturtle()
mainloop()
