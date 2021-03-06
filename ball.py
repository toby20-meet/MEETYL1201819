import turtle
import time
import random
from turtle import Turtle
#from ball.py import Ball
# turtle.penup()
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.shape("circle")
		self.pu()
		self.setposition(x,y)
		#self.x = x
		#self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r
		#self.color = color
		self.shapesize(self.r/10)
		self.color(color)
	def move(self,screen_width,screen_height):
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		up_side_ball = new_y + self.r
		down_side_ball = new_y - self.r
		self.goto(new_x,new_y)
		if right_side_ball >= screen_width:
			self.dx = -self.dx
		if up_side_ball >= screen_height:
			self.dy = -self.dy
		if left_side_ball <= -screen_width:
			self.dx = -self.dx
		if down_side_ball <= -screen_height:
			self.dy = -self.dy 

class Polygon(Turtle):
	def __init__(self,lines,color,size,x,y):
		Turtle.__init__(self)
		self.lines = lines
		self.r = size
		self.shapesize(size/10)
		self.pu()
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
		self.setposition(x,y)