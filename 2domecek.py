from turtle import left, right, forward, speed, goto, penup, pendown, setup
from turtle import exitonclick
from math import sqrt

setup(width=1100, height=800)
speed(8)
penup()
goto(-400, 0)
pendown()


def domek(strana):
# vypocet delky zakladny u pravouhleho trojuhelniku
    zakladna = sqrt(2)*strana
    left(90)
    forward(strana)
    right(30)
    forward(strana)
    right(120)
    forward(strana)
    right(30)
    forward(strana)
    right(135)
    forward(zakladna)
    right(135)
    forward(strana)
    right(135)
    forward(zakladna)
    left(135)
    forward(strana+20)


domek(20)
domek(40)
domek(60)
exitonclick()
