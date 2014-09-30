#Harry Derouich
#30/09/14
#Which number is larger?

number1 = int(input("Please enter your first number: "))
number2 = int(input("Please enter your second number: "))
if number1 > number2:
    print("The larger number is: {0}".format(number1))
elif number2 > number1:
    print("The larger number is: {0}".format(number2))
else:
    print("The numbers are the same, please try again")
