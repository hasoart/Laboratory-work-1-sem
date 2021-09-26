import turtle
n = 12
c=n
turtle.speed(10)
while n>0:
	turtle.forward(50)
	turtle.left(180)
	turtle.stamp()
	turtle.forward(50)
	turtle.left(180)
	turtle.left(360/c)
	n += -1
