import turtle as t
a = 10
t.speed(10)
t.setheading(90)
for i in range(5):
	for i in range(36):
		t.forward(a)
		t.left(10)
	for i in range(36):
		t.forward(a)
		t.right(10)
	a = a+1
