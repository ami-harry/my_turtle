import turtle as tr
t=tr.Turtle()
t.pensize(2)
s=tr.Screen()
t.shape('turtle')
s.title('4 circle bnayega ye')
col_lst=['red','yellow','green','blue']

t.up()
t.fd(200)
'''
for i in range(4):
	t.begin_fill()
	t.down()
	t.fillcolor(col_lst[i])
	t.circle(50)
	t.end_fill()
	t.up()
	t.bk(100)
'''	
'''
#creating pen wide->mtlb mota mota line
for i in range(4):
	
	t.down()
	t.pencolor(col_lst[i])
	t.pensize(20)
	t.circle(50)
	t.up()
	t.bk(100)
'''


tr.done()
