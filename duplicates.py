list = ["a", "a", "b", "b"]

while True:
    if list.count("a") + 1:
        list.remove("a")
    elif list.count("b") + 1:
        list.remove("b")
    else:
        break

print(list)


