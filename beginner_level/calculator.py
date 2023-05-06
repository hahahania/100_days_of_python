import os
from time import sleep


def addition(a, b):
    return a + b


def substraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


functions = {"+": addition, "-": substraction, "/": division, "*": multiplication}


def calculate():
    a = int(input("Enter first number :  "))
    calculation = True
    while calculation:
        sign = input("Choose sign of the operation :\n+\t-\t*\t/\n")
        b = int(input("Enter second number :  "))

        result = functions[sign](a, b)
        print(f"The result is : \n{a}{sign}{b}={result}")

        if (
            input(
                f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
            )
            == "y"
        ):
            a = result
        else:
            calculation = False
            sleep(1)
            os.system("clear")
            if input("Do you want to continue? (y/n)\t") == "n":
                break
            calculate()


calculate()
