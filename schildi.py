import turtle 

window = turtle.Screen()
turtle.shape("turtle")
size = 0

def fibonacci(index):
    if index == 0 or index == 1:
        return 1
    else:
        return fibonacci(index - 2)+ fibonacci(index-1)

while True:
    for x in range(0,4):
        turtle.speed(x + 50)
        turtle.forward(fibonacci(size))
        turtle.right(90)
    turtle.left(5)
    size += 1

window.mainloop()