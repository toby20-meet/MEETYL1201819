import turtle
import time
import random
import math
from ball import Ball
# turtle.colormode(255)
turtle.tracer(0,0)
turtle.hideturtle()
RUNNING = True 
SLEEP = 0.0077

SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

lines_width = int(1852/50)
liner = turtle.Turtle()
liner.pu()
liner.setposition(-926,512)
liner.pencolor(22/255,72/255,164/255)
#liner.hideturtle()
for i in range(0,lines_width+100):
	liner.pd()
	liner.goto(liner.xcor(),liner.ycor()-1024)
	liner.pu()
	liner.setposition(liner.xcor()+lines_width,512)
lines_height = int(1024/30)
liner.setposition(-926,512)
for i in range(0,lines_height):
	liner.pd()
	liner.goto(liner.xcor()+1852,liner.ycor())
	liner.pu()
	liner.setposition(-926,liner.ycor()-lines_height)
NUMBER_OF_BALLS = 10
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 50
MINIMUM_BALL_DX = -1
MAXIMUM_BALL_DX = 1
MINIMUM_BALL_DY = -1
MAXIMUM_BALL_DY = 1

NUMBER_OF_FOODS = 30
FOOD_RADIUS = 5

FOODS = []
BALLS = []

MY_BALL = Ball(0,0,5,0,20,"pink")

for i in range(NUMBER_OF_FOODS):
	x = random.randint(-SCREEN_WIDTH + FOOD_RADIUS, SCREEN_WIDTH - FOOD_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + FOOD_RADIUS,SCREEN_HEIGHT - FOOD_RADIUS)
	color = (random.random(),random.random(),random.random())
	new_food = Ball(x,y,0,0,FOOD_RADIUS,color)
	FOODS.append(new_food)
for i in range(NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = 0
	while dx == 0:
		dx = random.uniform(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy = 0
	while dy == 0:
		dy = random.uniform(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = (random.random(),random.random(),random.random())
	new_ball = Ball(x,y,dx,dy,radius,color)
	BALLS.append(new_ball)

def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def show_score():
	tscore = turtle.Turtle()
	#tscore.hideturtle()
	tscore.setposition(850,470)
	turtle.write("Score:"+score,True,"center",("Arial",10,"normal"))
def check_balls_eating():
	for ball in BALLS:
		for food in FOODS:
			if collide(ball,food):
				x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				color = (random.random(),random.random(),random.random())
				food.setposition(x,y)
				food.color(color)
				ball.r += 1
				ball.shapesize(ball.r/10)

def check_myball_eating():
	for food in FOODS:
		if collide(MY_BALL,food):
			x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			color = (random.random(),random.random(),random.random())
			food.setposition(x,y)
			food.color(color)
			MY_BALL.r += 1
			MY_BALL.shapesize(MY_BALL.r/10)

def collide(ball_a,ball_b):
	if ball_a == ball_b:
		return False
	Distance = math.sqrt(math.pow((ball_a.xcor()-ball_b.xcor()),2)+math.pow(ball_a.ycor()-ball_b.ycor(),2))
	if Distance+10 <= ball_a.r+ball_b.r:
		return True
	else:
		return False

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b):
				radius_a = ball_a.r
				radius_b = ball_b.r
				x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				dx = 0
				while dx == 0:
					dx = random.uniform(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				dy = 0
				while dy == 0:
					dy = random.uniform(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				color = (random.random(),random.random(),random.random())
				if radius_a <= radius_b:
					ball_a.setposition(x,y)
					ball_a.dx = dx
					ball_a.dy = dy
					ball_a.color(color)
					ball_b.r += int(ball_a.r/4)
					ball_a.r = radius
					ball_a.shapesize(ball_a.r/10)
					ball_b.shapesize(ball_b.r/10)
				else:
					ball_b.setposition(x,y)
					ball_b.dx = dx
					ball_b.dy = dy
					ball_b.color(color)
					ball_a.r += int(ball_b.r/4)
					ball_b.r = radius
					ball_a.shapesize(ball_a.r/10)
					ball_b.shapesize(ball_b.r/10)

def check_myball_collision():
	for ball in BALLS:
		if collide(ball,MY_BALL):
			radius_my = MY_BALL.r
			radius_alien = ball.r
			if radius_my < radius_alien:
				print(radius_my, radius_alien)
				print(MY_BALL.pos(), ball.pos())
				return False
			else:
				x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				dx = 0
				while dx == 0:
					dx = random.uniform(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				dy = 0
				while dy == 0:
					dy = random.uniform(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				color = (random.random(),random.random(),random.random())
				ball.setposition(x,y)
				ball.dx = dx
				ball.dy = dy
				ball.r = radius
				ball.color(color)
				MY_BALL.r += int(ball.r/4)
				MY_BALL.shapesize(MY_BALL.r/10)
				ball.shapesize(ball.r/10)
	return True
def move_around(event):
	MY_BALL.goto(event.x - SCREEN_WIDTH, SCREEN_HEIGHT - event.y)
turtle.getcanvas().bind("<Motion>", move_around)
turtle.listen()
while RUNNING:
	score = MY_BALL.r-20
	RUNNING = check_myball_collision()
	if SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2:
		SCREEN_WIDTH = int(turtle.getcanvas().winfo_width()/2)
		SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height()/2)
	print(SCREEN_WIDTH)
	print(SCREEN_HEIGHT)
	move_all_balls()
	check_myball_eating()
	check_balls_eating()
	check_all_balls_collision()
	check_myball_collision()
	turtle.update()
	time.sleep(SLEEP)
#add score and viruses