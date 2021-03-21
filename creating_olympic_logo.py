import turtle
t=turtle.Pen()


t.pensize(10)


#creating first circle
t.up()
t.home()
t.fd(100)
t.down()
t.color('red')
t.circle(50)


#creating second circle
t.up()
t.home()
t.goto(40,-40)
t.down()
t.color('green')
t.circle(50)

#creating third circle
t.up()
t.home()
t.goto(-20,0)
#t.bk(-20)
t.down()
t.color('black')
t.circle(50)


#creating third circle
t.up()
t.home()
t.goto(-140,0)
t.down()
t.color('blue')
t.circle(50)
t.up()
t.home()

t.goto(-80,-40)
t.down()
t.color('yellow')
t.circle(50)

turtle.done()
