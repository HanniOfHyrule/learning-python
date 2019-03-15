import turtle 

window = turtle.Screen()
turtle.shape("turtle")

while True:
    for x in range(0,4):
        turtle.speed(x + 50)
        turtle.forward(100)
        turtle.right(90)
    turtle.left(5)


window.mainloop()