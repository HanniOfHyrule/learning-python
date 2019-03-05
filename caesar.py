import sys

key = int(sys.argv[1])

# define function
def encrypt(char,key):
    if ord(char) >= 65 and ord(char) <= 122:
        encrypted = ord(char) + key
        if encrypted >122:
            return chr(encrypted - 122 + 65 -1)
        else:
            return chr(ord(char) + key)
    else:
        return char

for line in sys.stdin:
    result = []
    for char in list(line):
        result.append(encrypt(char,key))
    print("".join(result))