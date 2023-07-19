def hello():
    name = input("name: ")
    print("Hello " + name)
hello()
a = int(input("A: "))
b = int(input("B: "))
def sum(a,b):
    return a + b
c = sum(a,b)
d = 2
e = sum(c,d)
print(e)

def duplicates(a, b, c, d):
    list = [a, b, c, d]
    for i in list:
        while list.count(i) > 1:
            list.remove(i)
    return list

def calc(a,b):
    sum = a + b
    sub = a - b
    mult = a * b
    div = a / b
    return sum, sub, mult, div
print(calc(3,5))

def list(*args):
    for i in args:
        print(i)
list(10,20)


def outer_fun(a,b):
    square = a ** 2

    def addition(a,b):
        return a + b
    add = addition(a,b)
    return add +7
print(outer_fun(4,6))

def mosquito():
    hateness = input("How much do you hate mosquitos(0-10)?")
    
    def subtract(x):
        for i in range(x,0,-1):
            print(i)
        print("Mosqiuto Killed!")
    subtract(hateness)

mosquito()
            



        


                    
    

    

    

#A = int(input("First integer: "))
#B = int(input("Second integer: "))
#print(calc(A,B))

# def function name(argument):
    # print
    # return
