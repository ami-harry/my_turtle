import turtle as tr
t=tr.Pen()
t.pensize(5)

def draw_circle(x,y,r,col):
	t.begin_fill()
	t.up()
	t.goto(x,y)
	t.down()
	t.fillcolor(col)
	t.circle(r)
	t.end_fill()
	t.up()
	t.home()

rad=50
draw_circle(0,-rad,rad,"red")
draw_circle(200,200,rad,"yellow")
draw_circle(-200,200,rad,"orange")
draw_circle(-200,-200,rad,"blue")
draw_circle(200,-200,rad,"black")
t.up()


#creating the axis line

#x positive
t.down()
t.forward(rad*6) #
t.up()
t.home()

#x negative coordinate
t.down()
t.left(180)
t.forward(rad*6) 
t.up()
t.home()


#y positive coordinate
t.down()
t.left(90)
t.forward(rad*6) 
t.up()
t.home()


#y negative coordinate
t.down()
t.right(90)
t.forward(rad*6) 
t.up()
t.home()

tr.done()


