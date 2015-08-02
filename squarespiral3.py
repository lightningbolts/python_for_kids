__author__ = 'lightningbolts'
import turtle
t = turtle.Pen()
colors = ['red', 'blue', 'green', 'orange', 'pink', 'yellow']
for x in range(100):
    t.pencolor(colors[x % 6])
    t.forward(1.3 * x)
    t.left(61)
