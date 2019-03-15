import turtle 

window = turtle.Screen()
turtle.shape("turtle")
size = 1
turtle.pensize(0.4)

while True:
    for x in range(0,4):
        turtle.speed(x + 50)
        turtle.forward(size)
        turtle.right(90)
    turtle.left(5)
    size += 1

window.mainloop()