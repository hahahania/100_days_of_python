print("Welcome to the tip calculator")
total = int(input("What was the total bill?\t"))
percentage = int(
    input('What percentage tip would you like to givr? 10, 12 or 15?\t'))
people = int(input('How many people to plit the bill?\t'))
result = (total * (1+percentage/100))/people
print(f'Each person should pay : ${round(result,2)}')
