import turtle

turtle.shape('turtle')
for i in range (1, 11, 1):
	turtle.forward(i*20)
	turtle.left(90)
	turtle.forward(i*20)
	turtle.left(90)
	turtle.forward(i*20)
	turtle.left(90)
	turtle.forward(i*20)
	turtle.setheading(0)
	turtle.penup()
	turtle.goto(-i*10, -i*10)
	turtle.pendown()


	
