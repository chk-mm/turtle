from turtle import Turtle

t = Turtle()


def draw_sqaure(size):
    sq_iteration = 0
    while sq_iteration < 4:
        t.dot()
        t.pu()
        t.color('red')
        t.forward(size)
        t.left(90)
        sq_iteration = sq_iteration+1


size_sq = int(input('Input your desired size of square:'))
draw_sqaure(size_sq)



t.screen.mainloop()
