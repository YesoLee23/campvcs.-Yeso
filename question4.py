string = input("String: ")
string2 = ""

for i in range(len(string)):
    if i%2 == 1:
        string2 = [i]

print(string2)