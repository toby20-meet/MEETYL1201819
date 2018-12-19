import turtle
def make_circle(color,x,y,degree,heading):
	turtle.penup()
	turtle.setheading(heading)
	turtle.pensize(15)
	turtle.goto(x,y)
	turtle.pendown()
	turtle.color(color)
	turtle.circle(-100,degree)
make_circle('blue',0,0,325,180)
make_circle('yellow',220,-20,235,270)
make_circle('yellow',120,75,60,0)
make_circle('black',240,0,60,180)
make_circle('black',145,100,250,90)
make_circle('green',455,-20,250,270)
make_circle('green',365,75,60,0)
make_circle('red',385,95,325,90)
turtle.mainloop()

#Due to the amazingness of this code, sadek told me I don't need to do the rest of the lab!!!!! :D