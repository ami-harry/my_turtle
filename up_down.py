#Turtle is also aliases as Pen
#t.up() -> it will not draw any shape-> blank
#t.down()-> it will draw
#goto()--> x and y, x is must , y can be avoid



import turtle as tr
t=tr.Pen() #Turtle/ Pen both are same
t.right(90)
t.up() # it will cause not to draw any shape will turtle is moving
t.forward(100)
t.left(90)
t.down() # it will make turtle to draw while moving
t.circle(100)

tr.done()

#up()--> it leaves blank


#t.undo()--> it will take one step back
#t.reset() -> it will reset everything
