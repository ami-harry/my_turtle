#drawing indian flag using turtle

import turtle
t=turtle.Pen()
t.pensize(2)
s=turtle.Screen()
s.title("ye turtle hai and ye hmari flag bn rahyiee haii")

#drawing the line first
t.up()
t.home()
t.down()
t.right(90)
t.fd(200)
t.up()
t.home()
t.left(90)
t.down()
t.fd(300)
t.up()
t.home()

#creating 3 boxes
t.goto(0,300)
t.begin_fill()
t.pencolor('black')
t.fillcolor('orange')
t.down()
t.fd(400)
t.right(90)
t.fd(100)
t.right(90)
t.fd(400)
t.end_fill()
t.up() #orange box complete

t.home()
t.goto(0,200)
t.down()
t.fd(400)
t.right(90)
t.fd(100)
t.right(90)
t.fd(400) #middle box complete
t.up()

#drawing the circle
t.goto(200,100)
t.down()
t.color('blue')
t.circle(-50)
t.up()

#drawing lines
t.goto(200,100)
t.down()
t.setheading(90) #it will goto center of the circle
t.up()
t.fd(50)
for i in range(24):
	t.down() #drawing the lines
	t.fd(50)
	t.bk(50)
	t.left(15)
	



t.up()
t.home()
t.goto(0,100)
t.down()
t.pencolor('black')
t.begin_fill()
t.fillcolor('green')
t.fd(400)
t.right(90)
t.fd(100)
t.right(90)
t.fd(400)
t.end_fill()# green box complete
t.up()






#creating the ladders
t.home()
t.goto(0,-200)
t.down()
t.fd(50)
t.right(90)
t.fd(25)
t.right(90)
t.fd(100)
t.right(90)
t.fd(25)
t.right(90)
t.fd(50)
t.up()

#creating 2nd ladder
t.home()
t.goto(0,-225)
t.down()
t.fd(80)
t.right(90)
t.fd(40)
t.right(90)
t.fd(160)
t.right(90)
t.fd(40)
t.right(90)
t.fd(40)
t.up()

#creating 3nd ladder
t.home()
t.goto(0,-265)
t.down()
t.fd(120)
t.right(90)
t.fd(60)
t.right(90)
t.fd(240)
t.right(90)
t.fd(60)
t.right(90)
t.fd(120)
t.up()
turtle.done()
