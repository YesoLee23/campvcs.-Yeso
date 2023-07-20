greeting = input("Greeting: ")

def bank(string):
    if greeting == ("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$120")
    else:
        print("$100")
bank(greeting)


