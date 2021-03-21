import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('pink')
t.shape('turtle')
t.speed(1)
t.begin_fill()
s.title('bhai turtle shape bna rha hai')
i=1
while i<=2:

	#drawing the circle with red
	t.fillcolor('red')
	t.circle(50)
	t.end_fill()

	#drawing triangle
	#changing the position 
	t.goto(100,0)
	t.begin_fill()
	t.fillcolor('yellow')
	t.circle(50,steps=3)
	t.end_fill()

	#drawing square
	#changing the position 
	t.goto(0,0)
	t.goto(0,-100)
	t.begin_fill()
	t.fillcolor('green')
	t.circle(50,steps=4)
	t.end_fill()


	#drawing pentagon
	#changing the position 
	t.goto(0,-50)
	t.goto(100,-100)
	t.begin_fill()
	t.fillcolor('blue')
	t.circle(50,steps=5)
	t.end_fill()



	#drawing hexagon
	#changing the position 
	t.goto(0,-100)
	t.goto(0,-200)
	t.begin_fill()
	t.fillcolor('black')
	t.circle(50,steps=6)
	t.end_fill()


	#drawing septagon
	#changing the position 
	t.goto(0,-100)
	t.goto(100,-200)
	t.begin_fill()
	t.fillcolor('orange')
	t.circle(50,steps=7)
	t.end_fill()
	i+=2
	if 1:
		t.undo()
	
turtle.done()

