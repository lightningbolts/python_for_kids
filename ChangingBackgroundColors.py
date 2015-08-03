__author__ = 'lightningbolts'
import turtle
t = turtle.Pen()
turtle.bgcolor('black')
colors = ['red', 'white']
for x in range(215):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(90)