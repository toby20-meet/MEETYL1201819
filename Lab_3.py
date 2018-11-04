import turtle
'''
x = 0
while x < 5:
	turtle.forward(100)
	turtle.right(144)
	x += 1


turtle.mainloop()
'''
'''
turtle.begin_fill()
turtle.forward(50)
turtle.right(90)
turtle.forward(25)
turtle.right(45)
turtle.forward(40)
turtle.end_fill()
turtle.begin_fill()
turtle.penup()
turtle.goto(0,0)
turtle.left(315)
turtle.pendown()
turtle.left(90)
turtle.forward(25)
turtle.left(45)
turtle.forward(40)
turtle.end_fill()
'''
turtle.register_shape("index.gif")
turtle.shape("index.gif")
turtle.speed(1000)
asd = 0
for i in range(360):
	turtle.right(asd)
	turtle.forward(200)
	turtle.right(45)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(50)
	turtle.penup()
	turtle.home()
	turtle.pendown()
	asd = asd + 1

turtle.mainloop()