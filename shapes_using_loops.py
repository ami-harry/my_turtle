import turtle
t=turtle.Turtle()
s=turtle.Screen()
t.shape('turtle')

s.title("khud shape change hoga")
s.bgcolor('pink')

t.begin_fill()
turtle.colormode(255)

#s.bgcolor(r,g,b)

sh=50
sz=40
for a in range(3,20):
	sz+=10
	t.circle(sz,steps=int(a))
	t.fillcolor('red')

	
t.end_fill()
	
turtle.done()

