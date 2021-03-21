import turtle as t
tut_object=t.Turtle() 
#here we have to draw square , we have to do same process for four time
#setting background color
sc_obj=t.Screen()
sc_obj.bgcolor("black")
tut_object.color("yellow") #setting the turtle object color


tut_object.begin_fill()
t.title("square")
tut_object.speed(1) #0 is fastest , range is 0 to 10
tut_object.hideturtle() #this will hide the turtle


#col=input("Enter color name: ")
tut_object.fillcolor("white") ##we can fill color into the object at,default color is black

for i in range(4):
	tut_object.fd(100)
	tut_object.left(90)

tut_object.end_fill()
t.done()
