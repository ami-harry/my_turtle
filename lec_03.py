import turtle as t
tut_obj=t.Turtle()
# the turtle object moves along axis, the initial position is (0,0)
# the original direction of turtle is right direction, we can chage it bye setdirection method, by giving value in degress

#           east
#             |
#             |
# south <--------------> north (default turtle position)
#             |
#             |
#           west


t.setheading(90)
t.fd(100)
t.setheading(180)
t.fd(200)
t.setheading(270)
t.fd(300)
t.setheading(0)
t.fd(300)

t.done()