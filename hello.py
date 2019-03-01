def find_greeting(name):
    if name == "Felix":
        print("Hello Felix, wahhhhhhh")
    elif name == "Dominik":
        print("Hello Dominik, i love you. You are amazing")
    elif name == "Johanna":
        print("Hello Johanna, how are you?")
    else:
        print( "Hello " + name + ", nice to meet you!")

with open("names.txt", "rU") as f:
    for line in f:
        find_greeting(line.rstrip())
 