import turtle 

window = turtle.Screen()
turtle.shape("turtle")

for x in range(0,4):
    turtle.speed(x + 1)
    turtle.forward(100)
    turtle.right(90)

window.mainloop()