#drawing heart shape 

import turtle
t=turtle.Pen()

#we will do it in 4 part

#first draw the line and then semi circle and then change the angle and again semicircle then complete the line
t.begin_fill()
t.left(140) #moving the cursor to left to draw the line
t.fd(200) 
t.circle(-100,200) #making circle in clockwise direction so the value is in -ve and we want more than semi circle so we have took 200 deg
t.setheading(60) #moving the heading to draw the 3rd part, another semi circle
t.circle(-100,200)
t.fillcolor('red')
t.fd(200) # this will complete the heart shape
t.end_fill()

turtle.done()
