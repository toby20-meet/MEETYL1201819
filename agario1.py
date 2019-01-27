
import turtle
import time
import random
from ball import *
from turtle import *
colormode(255)
turtle.tracer(0)
turtle.hideturtle()
running = True
sleep = 0.0077
screen_width =turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2
number_of_BALLS = 7
minimum_ball_radius = 10
maximum_ball_radius = 60
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5
score = 0
balls = []
big_ball = Ball(100,100,5,5,50,"blue")

scoret = turtle.Turtle()

for i in range (number_of_BALLS):
	screen_random1_x = int(-screen_width+maximum_ball_radius)
	screen_random2_x = int(screen_width-maximum_ball_radius)
	random_x = random.randint(screen_random1_x,screen_random2_x)
	
	screen_random1_y = int(-screen_height+maximum_ball_radius)
	screen_random2_y = int(screen_height-maximum_ball_radius)
	random_y = random.randint(screen_random1_y,screen_random2_y)
	
	random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
	while random_dx == 0:
		random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)

	random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
	while random_dy == 0:
		random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
	radius = random.randint(minimum_ball_radius,maximum_ball_radius)

	color = (random.randint(0,250), random.randint(0,250), random.randint(0,250))
	

	ball = Ball(random_x,random_y,random_dx,random_dy,radius,color)
	balls.append(ball)


def move_all_balls():
	for b in range(number_of_BALLS):
		balls[b].move(screen_width,screen_height)

def check_collide(ball_a,ball_b):
	if ball_a == ball_b:
		return False
						#squareroot ( x2-x1 squared ) + ( y2-y1 squared)
	balls_distance = ((ball_a.xcor()-ball_b.xcor())**2 +(ball_a.ycor()-ball_b.ycor())**2)**0.5

	if balls_distance+10 <= (ball_a.r+ball_b.r):
		return True 
	else:
		return False

def check_all_balls_collision():
	for ball_a in balls:
		for ball_b in balls:
			if check_collide(ball_a,ball_b) == True:
				radius1 = ball_a.r
				radius2 = ball_b.r
				random_x = random.randint(screen_random1_x,screen_random2_x)
				random_y = random.randint(screen_random1_y,screen_random2_y)
				random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
				while random_dx == 0:
					random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
				random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
				while random_dy == 0:
					random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
				radius = random.randint(minimum_ball_radius,maximum_ball_radius)
				color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

				if radius1 > radius2:
					ball_b.goto(random_x,random_y)
					ball_b.dx = random_dx
					ball_b.dy = random_dy
					ball_b.r = radius
					ball_b.shapesize(ball_b.r/10)
					ball_b.color = color
					ball_a.r += 0.5
					ball_a.shapesize(ball_a.r/10)
					
				elif radius1 < radius2:
					ball_a.goto(random_x,random_y)
					ball_a.dx = random_dx
					ball_a.dy = random_dy
					ball_a.r = radius
					ball_a.shapesize(ball_a.r/10)
					ball_a.color = color
					ball_b.r += 0.5
					ball_b.shapesize(ball_b.r/10)
					
def check_myball_collision():	
	global score , scoret		
	for ball in balls:
		random_x = random.randint(screen_random1_x,screen_random2_x)
		random_y = random.randint(screen_random1_y,screen_random2_y)
		random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
		while random_dx == 0:
			random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
		random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
		while random_dy == 0:
			random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
		radius = random.randint(minimum_ball_radius,maximum_ball_radius)
		color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
		if check_collide(big_ball,ball) == True:
			radius33 = big_ball.r
			radius44 = ball.r

			if radius33 < radius44:
				print("you lost SORRY!")
				return 	False
			else:
				big_ball.r += 2
				big_ball.shapesize(big_ball.r/10)
				if score == 100:
					print('YOU WON WOHOO!!')
					scoret.pu()
					scoret.goto(0,250)
					scoret.clear()
					scoret.write("your score is : " + str(score),align="center",font=("Arial", 20, "normal"))
					scoret.goto(0,0)
					scoret.write(" OH YOU WON!", align="center",font=("Arial", 100 ,"normal"))
					
				else:
					score += 1
					scoret.pu()
					scoret.goto(0,250)
					scoret.clear()
					scoret.write("your score is : " + str(score),align="center",font=("Arial", 20, "normal"))
					ball.goto(random_x,random_y)
					ball.dx = random_dx
					while ball.dx == 0:
						ball.dx = random.randint(minimum_ball_dx,maximum_ball_dx)
					ball.dy = random_dy
					while ball.dy == 0:
						ball.dy = random.randint(minimum_ball_dy,maximum_ball_dy)
					ball.r = radius
					ball.shapesize(ball.r/10)
					ball.color = color
	return True

def movearound(event):	
	x1 = event.x - screen_width
	y1 = screen_height - event.y
	big_ball.goto(x1,y1)
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while running == True:
	if screen_width !=  int(turtle.getcanvas().winfo_width()/2) or screen_height != int(turtle.getcanvas().winfo_height()/2):
		screen_width =int(turtle.getcanvas().winfo_width()/2)
		screen_height = int(turtle.getcanvas().winfo_height()/2)
	move_all_balls()
	check_all_balls_collision()
	if check_myball_collision() == False:
		running = False
		turtle.goto(0,0)
		turtle.write("you lost SORRY!!",align="center",font=("Arial", 100, "normal"))
		print("COLLIDING")
		#turtle.bye()
	getscreen().update()
	time.sleep(sleep)



mainloop()