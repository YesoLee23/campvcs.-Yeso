print("Welcome to Yeso's calculator\n")

# get x and y from users
# define as integers
x = int(input('What is your first integer?'))
y = int(input('What is your second integer?'))

# get add, subtract, multiply or divide
math = input("What would you like to do with these numbers?")

# if add, subtract, multiply or divide, compute answer
if math == "add":
    print( x, "+", y, x+y)
if math == "subtract":
    print( x, "-", y, x-y)
if math == "multiply":
    print( x, "*", y, x*y)
if math == "divide":
    print( x, "/", y, x/y)
