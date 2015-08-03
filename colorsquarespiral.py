__author__ = 'lightningbolts'
import turtle
import random
t = turtle.Pen()
colors = ['red', 'yellow', 'blue', 'green']
for x in range(150,1,-1):
    t.pencolor(random.choice(colors))
    t.forward(x)
    t.right(185)
    t.backward(100)
    t.left(99)
