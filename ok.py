# from turtle import *
import turtle as nitish
import random

t = nitish.Pen()  # turtle.Turtle()
# s = nitish.Screen()
# s.bgcolor('pink')
# s.bgpic('pic.gif')
# t.fd(100) #forward
# t.backward(200) #bk

# t.setheading(90)
t.speed(1)
t.shape('turtle')
# t.left(23)
# t.fd(100)
# t.right(125)

# t.fd(100)
# t.setheading(100)
# t.fd(100)

# t.up()
# t.fd(100)

# t.fd(100)
# t.down()
# t.right(100)
# t.fd(100)
# t.shape('sqaure/circle/turtle')


# t.circle(50,270) #(radius,degree)
# t.circle(100,steps=10)
'''
t.begin_fill()
t.fillcolor('red')
t.circle(100, steps=3)
t.end_fill()
'''

# t.up()
# t.goto(100, 100)
# t.down()
# t.color('blue')
# t.circle(50)
'''
t.up()
t.goto(50, -40)
t.down()
t.color('blue')
t.circle(-50, 180)
t.up()
t.home()  # it will take the turtle to 0,0
t.goto(50, -140)
t.down()
t.color('red')
t.circle(50,-180)
t.up()
t.home()  # it will take the turtle to 0,0
'''


# 360
# 90
# 90
# 90
# 90
'''
t.up()
t.color('red')
t.down()
t.circle(-50, 90)
t.color('pink')
t.circle(-50, 90)
t.color('yellow')
t.circle(-50, 90)
t.color('blue')
t.circle(-50, 90)
'''


# usiing for loop
col = ['red', 'blue', 'green', 'pink', 'orange']
deg = 15
for i in range(24):
    t.up()
    t.goto(50, -40)
    t.down()
    # t.color(random.random(len(col[i])))
    t.circle(-100, 360/deg)


nitish.done()
