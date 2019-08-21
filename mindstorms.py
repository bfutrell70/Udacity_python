import turtle

def draw_square(some_turtle):
	x = 0
	while x < 4:
		some_turtle.forward(100)
		some_turtle.right(90)
		x = x + 1

def draw_diamond(some_turtle):
	for i in range(2):
		some_turtle.forward(100)
		some_turtle.right(45)
		some_turtle.forward(100)
		some_turtle.right(135)

def draw_petal(some_turtle):
	for i in range(6):
		some_turtle.forward(100)
		some_turtle.right(60)
			
def draw_circle():
	angie = turtle.Turtle()

	angie.shape("arrow")
	angie.color("blue")
	angie.circle(100)

def draw_triangle():
	suzie = turtle.Turtle()
	suzie.shape("classic")
	suzie.color("green")
	
	x = 0
	while x < 3:
		suzie.forward(100)
		suzie.right(120)
		x = x + 1

def draw_flower(some_turtle):
	#some_turtle.forward(100)
	some_turtle.shape("triangle")
	some_turtle.color("yellow")
	some_turtle.speed(20)
	for i in range(36):
		#draw_petal(some_turtle)
		draw_diamond(some_turtle)
		some_turtle.right(10)
			
	some_turtle.color("green")
	some_turtle.right(90)
	some_turtle.forward(300)
						
def draw_shapes():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	draw_flower(brad)
	#for i in range(1,37):
	#	draw_square(brad)
	#	brad.right(10)
	
	#draw_circle()
	#draw_triangle()
	window.exitonclick()
						
			
draw_shapes()