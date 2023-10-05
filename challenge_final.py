from turtle import Turtle
import random

t = Turtle()

def replicate_polkadot_nxn(nsq):
    for x in range(nsq):
        i = 0
        n = nsq
        while i < n:
            colors = random.choice(
                ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue',
                 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray'])
            t.dot()
            t.color(colors)
            t.pu()
            t.forward(50)
            i += 1
        if x % 2 == 0:
            t.right(90)
        else:
            t.left(90)
        t.pu()
        t.forward(25)
        if x % 2 == 0:
            t.right(90)
        else:
            t.left(90)
        t.pu()
        t.forward(50)

nsquare = input('Input ypur desired nxn sqaure:')
replicate_polkadot_nxn(int(nsquare))
t.screen.mainloop()