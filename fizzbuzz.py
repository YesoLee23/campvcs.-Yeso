x = int(input("Numer: "))

def fizzbuzz(x):
    if x%3 == 0:
        print("fizz", end="")
    if x%5 == 0:
        print("buzz")
        
    # if multiple of 3 print fizz
    # if multiple of 5 print buzz

fizzbuzz(x)