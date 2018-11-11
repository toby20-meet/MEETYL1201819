import turtle
import random
class Square(turtle):
	def __init__(self, size):
		self.shape("square")
		self.shapesize = size

	def random_color(self):
		self.color()
