class Drink:
    def __init__(
        self, name: str, price: float, water: int, coffee: int, milk: int
    ) -> None:
        self.name = name
        self.price = price
        self.water = water
        self.coffee = coffee
        self.milk = milk


class Machine:
    def __init__(self) -> None:
        self.water = 300
        self.coffee = 100
        self.milk = 200
        self.coins = 0

    def raport(self) -> str:
        return f"Current resources are:\n-{self.water}ml of water\n-{self.milk}ml of milk\n-{self.coffee}g of coffee\n-${self.coins}"

    def prepare_drink(self, drink: object):
        if self.check_resources(drink):
            if self.payment(drink):
                print(f"There is your {drink.name}, here you are :)")
                self.water -= drink.water
                self.coffee -= drink.coffee
                self.milk -= drink.milk
            else:
                print("You do not have enough money to pay.")

    def check_resources(self, drink: object) -> bool:
        if (
            drink.water > self.water
            or drink.coffee > self.coffee
            or drink.milk > self.milk
        ):
            print("There are not enough resources to prepare your coffee, sorry :(")
            return False
        else:
            return True

    def payment(self, drink: object):
        print("Please insert coins:")
        penny = float(input("How many pennies?  "))
        dime = float(input("How many dimes?  "))
        nickle = float(input("How many nickles?  "))
        quarters = float(input("How many quarters?  "))

        change = (
            penny * 0.01 + dime * 0.05 + nickle * 0.1 + quarters * 0.25 - drink.price
        )
        if change < 0:
            return False
        else:
            self.coins += drink.price
            print(f"Your change is ${round(change,2)}.")
            return True


latte = Drink("latte", 2.50, 200, 24, 150)
espresso = Drink("espresso", 1.50, 50, 18, 0)
cappuccino = Drink("cappuccino", 3.0, 250, 24, 100)

drinks = {"latte": latte, "espresso": espresso, "cappuccino": cappuccino}

coffe_machine = Machine()

buying = True

while buying:
    drink = input("Do you want to buy espresso, latte or cappuccino?  ").lower()
    if drink == "raport":
        print(coffe_machine.raport())
    else:
        coffe_machine.prepare_drink(drinks[drink])

    if input("Do you want anything else? (y/n)  ").lower() == "n":
        print("Thank you! Goodbye")
        buying = False
