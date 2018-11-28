import turtle
from turtle import Turtle
import random
turtle.colormode(255)
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
turtle.hideturtle()
class Hexagon(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
	def Shape(self):
		turtle.begin_poly()
		turtle.penup()
		for x in range(6):
			turtle.forward(10)
			turtle.left(60)
		turtle.end_poly()
		p = turtle.get_poly()
		turtle.register_shape("hexagon",p)
		self.shape("hexagon")
j = Hexagon(5)
j.Shape()
turtle.mainloop()