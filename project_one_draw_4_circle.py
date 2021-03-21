# we will draw 5 cicles here , 
#at (0,0), 
#at (200,200)
#at (-200,200)
#at (-200,-200)
#at (200,-200)


import turtle as tr
t=tr.Pen()

rad=50
t.up() #will make space, or will leave the blank while the turtle is moving
t.goto(0,-rad)
t.down()
t.begin_fill()

t.circle(rad)
t.fillcolor("green")
t.end_fill()
#here one circle is drawn and we will go to center
t.up()
#t.home()--> it will take the pointer to 0,0 position
t.home()


#at (200,200)
t.goto(200,200)
t.down()
t.begin_fill()
t.fillcolor("red")
t.circle(rad)
t.end_fill()
t.up()
t.home()

#at (-200,200)
t.goto(-200,200)
t.down()
t.begin_fill()
t.circle(rad)
t.fillcolor("orange")
t.end_fill()
t.up()
t.home()


#at (-200,-200)
t.goto(-200,-200)
t.begin_fill()
t.down()
t.circle(rad)
t.fillcolor("blue")
t.end_fill()
t.up()
t.home()

 

# at (200,-200)
t.goto(200,-200)
t.begin_fill()
t.down()
t.circle(rad)
t.fillcolor("yellow")
t.end_fill()
t.up()
t.home()


#creating the coordinate lines
t.down()
t.forward(rad*6) #+ve x coordinate
t.up()
t.home()

t.left(90)
t.down()
t.forward(rad*6) #+ve y coordinate
t.up()
t.home()

t.left(180)
t.down()
t.forward(rad*6) #-ve x coordinate
t.up()
t.home()

t.right(90)
t.down()
t.forward(rad*6) #-ve y coordinate
t.up()
t.home()



tr.done()
