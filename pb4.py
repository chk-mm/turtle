import turtle as t
import random

def random_walk(walk):
    for i in range(100):
        colors = random.choice(['orchid','red', 'brown', 'blue', 'orange', 'black', 'lightgreen'])
        angle = int(90)
        t.color(colors)
        t.setheading(random.choice([0,90,180,270]))

        t.fd(walk)
        print(i)

walksize = int(input('Input your desired steps of walk:'))
random_walk(walksize)