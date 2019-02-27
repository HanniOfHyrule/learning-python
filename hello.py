def find_greeting(name):
    if name == "Felix":
        print("Hello Felix, wahhhhhhh")
    elif name == "Dominik":
        print("Hello Dominik, i love you. You are amazing")
    elif name == "Johanna":
        print("Hello Johanna, how are you?")
    else:
        print( "Hello " + name + ", nice to meet you!")

while True:
    myname = input("What is your Name? ")
    find_greeting(myname)
