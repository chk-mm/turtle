from turtle import Turtle
t = Turtle()
t.speed(0)
for i in range(6):
    for color in ('orchid','red', 'brown', 'blue', 'orange', 'black', 'lightgreen'):
        t.color(color)
        t.circle(100)
        t.left(10)

t.screen.mainloop()

