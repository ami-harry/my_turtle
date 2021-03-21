import turtle
t=turtle.Turtle()
col=['yellow','pink','red','black','blue','green','orange']

def start_experiment():
	for i in range(200):
		t.color(col[i%7])
		t.pensize(i/10+1)
		t.fd(i)
		t.left(45)


start_experiment()
turtle.done()
