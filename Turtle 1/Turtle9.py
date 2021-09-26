import turtle as t
import math
d = 40
r = 40
for i in range(3,11):
    a = 2*r*math.sin(math.pi/i)
    a1 = 90+180/i
    a2 = 360/i
    t.penup()
    t.forward(d)
    t.pendown()
    t.left(a1)
    for z in range(i):
        t.forward(a)
        t.left(a2)
    t.right(a1)
    r += d
