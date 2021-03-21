# draw a square shape

import turtle as t
tut_object=t.Turtle()
t.title("Triangle")
t.speed(0) #-->0 is the fastest speed ,we can give it speed from 0 to 10

#to draw a right traingle
print("This will draw the triangle")
for i in range(3):
	tut_object.fd(100)
	tut_object.left(120)
tut_object.hideturtle() #this will hide turtle 
t.done()

