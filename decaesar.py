import sys 

key = int(sys.argv[1])

def decrypt(char,key):
    if ord(char) >= 65 and ord(char) <= 122:
        decrypted = ord(char) - key
        if decrypted <65:
            return chr(decrypted - 65 + 122 +1)
        else:
            return chr(decrypted)
    else:
        return char

for line in sys.stdin:
    result = []
    for char in list(line):
        result.append(decrypt(char,key))
    print("".join(result))