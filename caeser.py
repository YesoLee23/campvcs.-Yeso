# print(chr(ord('y')))
# print(ord(chr(121)))

key = int(input("key: "))
plaintext = input("plaintext: ")

for i in plaintext:
    print(chr(ord(i) + key),end = "")
    # change i to the number format
    # add the key
    # convert back to a character

for char in plaintext:
    if char.isupper():
        print(chr((ord(char) - 65 + key) % 26 + 65), end="")
    elif char.islower():
        print(chr((ord(char) - 97 + key) % 26 + 97), end="")
    else:
        print(char, end="")
print("")
 

  