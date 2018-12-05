from turtle import *
import random
import math
tracer(0)
colormode(255)
class Ball(Turtle):
	def __init__(self,radius,color,x,y,dx,dy):
		Turtle.__init__(self)
		self.pu()
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.goto(self.x,self.y)
	def move(self):
		posx = self.xcor()
		posy = self.ycor()
		newposx = posx + self.dx
		newposy = posy + self.dy
		self.goto(newposx,newposy)
		if(newposx+self.radius >= 460 or newposx-self.radius <= -460):
			self.dx = self.dx * -1
		if(newposy+self.radius >= 400 or newposy-self.radius <= -400):
			self.dy = self.dy * -1
a = Ball(29,"Blue",50,100,.20,.17)
b = Ball(30,"Red",200,-50,.22,.21)

def check_collision(ball1,ball2):
	C = math.pow(ball1.xcor()-ball2.xcor(),2) + math.pow(ball1.ycor()-ball2.ycor(),2)
	D = math.sqrt(C)
	if(D <= ball1.radius+ball2.radius):
		tempx = ball1.dx
		tempy = ball1.dy
		ball1.dx = ball2.dx
		ball1.dy = ball2.dy
		ball2.dx = tempx
		ball2.dy = tempy
		ball1.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
		ball2.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
		return True
while True:
	a.move()
	b.move()
	check_collision(a,b)
	if check_collision(a,b):
		tpx = random.randint(-400,400)
		tpy = random.randint(-350,350)
		if a.radius > b.radius:
			b.hideturtle()
			b.goto(tpx,tpy)
			b.showturtle()
		else:
			a.hideturtle()
			a.goto(tpx,tpy)
			a.showturtle()
	update()


mainloop()