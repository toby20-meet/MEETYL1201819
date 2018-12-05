import turtle
from turtle import Turtle
import random
turtle.colormode(255)
turtle.hideturtle()
turtle.speed(0)
'''
class Square(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)

	def random_color(self):
		self.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))

p = Square(50)
p.random_color()


'''
'''
class Hexagon(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
	#def Shape(self):
		turtle.begin_poly()
		turtle.penup()
		for x in range(6):
			turtle.forward(10)
			turtle.left(60)
		turtle.end_poly()
		p = turtle.get_poly()
		turtle.register_shape("hexagon",p)
		self.shape("hexagon")
j = Hexagon(3)
#j.Shape()
'''

class Polygon(Turtle):
	def __init__(self,lines,color,size):
		Turtle.__init__(self)
		self.lines = lines
		self.shapesize(size)
		self.color(color)
		turtle.begin_poly()
		turtle.penup()
		for i in range(self.lines):
			turtle.forward(20)
			turtle.right(360/self.lines)
		turtle.end_poly()
		p = turtle.get_poly()
		turtle.register_shape("Polygon",p)
		self.shape("Polygon")

d = Polygon(10,(126,55,200),7)



turtle.mainloop()