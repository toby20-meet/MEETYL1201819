import turtle
import time
import random
from turtle import Turtle
#from ball.py import Ball
# turtle.penup()
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.setposition(x,y)
		self.shape("circle")
		#self.x = x
		#self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r
		#self.color = color
		self.shapesize(self.r/10)
		self.color(color)
	def move(self,screen_width,screen_height):
		current_x = self.x
		new_x = current_x + dx
		current_y = self.y
		new_y = current_y + dy
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		up_side_ball = new_y + self.r
		down_side_ball = new_y - self.r
		self.goto(new_x,new_y)
		if right_side_ball >= screen_width:
			dx = -dx
		if up_side_ball >= screen_height:
			dy = -dy
		if left_side_ball <= -screen_width:
			dx = -dx
		if down_side_ball <= -screen_height:
			dy = -dy 
# turtle.mainloop()