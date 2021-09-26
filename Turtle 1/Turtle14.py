import turtle
import math
turtle.shape('turtle')
a = 300
def zvezda(n):
	a1 = 90-360/n
	a2 = 180-180/n
	turtle.penup()
	turtle.forward(a/(2*math.sin(2*math.pi/n)))
	turtle.right(a1)
	turtle.pendown()
	for i in range(n):
		turtle.forward(a)
		turtle.left(a2)
zvezda(11)