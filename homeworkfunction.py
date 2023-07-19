def homework():
    amount = input("How much homework do you have(0-10)?")

    def multiplication(amount,b):
        return amount * b
    mult = multiplication(amount,1)
    return mult *90
print("It will take" + homework + " hours to finish your homework!")