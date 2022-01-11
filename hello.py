def find_greeting(name):
    if name == "Felix":
        print("Hello Felix")
    elif name == "Dominik":
        print("Hello Dominik, you are amazing")
    elif name == "Johanna":
        print("Hello Johanna, how are you?")
    else:
        print( "Hello " + name + ", nice to meet you!")

with open("names.txt", "rU") as f:
    for line in f:
        find_greeting(line.rstrip())
 
