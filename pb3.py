from turtle import Turtle
import random

t = Turtle()

def draw_sqaure(size,n,speed):
    for i in range(3,n):
        sq_iteration = 0
        test = 360/i
        while sq_iteration < i:
            t.speed(speed)
            colors = random.choice(['red', 'brown', 'blue', 'orange','black','lightgreen'])
            t.color(colors)
            t.forward(size)
            t.left(test)
            sq_iteration = sq_iteration+1
    print('end of your drawing')


size = int(input('Input your desired size of square:'))
nsq = int(input('Input your n squares(3-10):'))
nsq = 10
speed = int(input('Input your turtle speed(0-10):'))
draw_sqaure(size,nsq,speed)



t.screen.mainloop()
