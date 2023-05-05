import os
from time import sleep

bidders = {}


def get_price(dictionary: dict):
    name = input("What's your name?\t")
    number = True
    while number:
        try:
            price = int(input("What's your bid?\t"))
            number = False
        except:
            print("You passed invalid format of bid value")
    dictionary[name] = price
    return


auction = True
while auction:
    get_price(bidders)
    decision = input("Are there any other bidders? (yes/no)   ").lower()
    if decision == "no":
        auction = False
    sleep(1)
    os.system("clear")
winner = max(bidders)
print(f"The winner is: {winner}\nThe price which will be paid: {bidders[winner]}")
