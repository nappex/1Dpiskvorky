from turtle import left, right, forward, speed, goto, penup, pendown
from turtle import exitonclick
from math import sqrt

speed(5)
strana = 50
zakladna = sqrt(2)*strana  # vypocet delky zakladny u pravouhleho trojuhelniku

penup()
goto(-450, 0)
pendown()

for i in range(10):
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
    forward(75)


exitonclick()
