# import turtle
# from turtle import teleport
from turtle import Turtle
t = Turtle()
# t.pen(fillcolor="black", pencolor="red", pensize=2)
t.setpos(180,180)
t.fillcolor('yellow')
t.begin_fill()
t.speed(0)
t.color('red')
t.circle(50)
t.end_fill()

# turtle.teleport(y=10)
t.goto(-180,-180)
t.fillcolor('yellow')
t.begin_fill()
t.speed(0)
t.color('yellow')
t.circle(50)
t.end_fill()

t.goto(0,0)
t.fillcolor('yellow')
t.begin_fill()
t.speed(0)
t.color('orchid')
t.circle(50)
t.end_fill()

t.goto(0,-175)
t.fillcolor('yellow')
t.begin_fill()
t.speed(0)
t.color('brown')
t.circle(50)
t.end_fill()

t.goto(0,175)
t.fillcolor('green')
t.begin_fill()
t.speed(0)
t.color('green')
t.circle(50)
t.end_fill()

t.goto(180,-175)
t.fillcolor('yellow')
t.begin_fill()
t.speed(0)
t.color('pink')
t.circle(50)
t.end_fill()


t.goto(180,0)
t.fillcolor('yellow')
t.begin_fill()
t.speed(0)
t.color('blue')
t.circle(50)
t.end_fill()

t.goto(-180,0)
t.fillcolor('yellow')
t.begin_fill()
t.speed(0)
t.color('lightblue')
t.circle(50)
t.end_fill()

t.goto(-180,180)
t.fillcolor('yellow')
t.begin_fill()
t.speed(0)
t.color('aquamarine')
t.circle(50)
t.end_fill()

t.teleport(0,0)

t.screen.mainloop()
