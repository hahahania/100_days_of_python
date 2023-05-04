import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
good = True
while good:
    try:
        num_letter = int(input('How many letters does password have?\t'))
        num_symbols = int(input('how many symbols are in the password?\t'))
        num_numbers = int(input('how many numbers are in the password?\t'))
        good = False
    except:
        print('incorrect type of input, try again')
password = []
for i in range(num_letter):
    password.append(random.choice(letters))
for i in range(num_symbols):
    password.append(random.choice(symbols))
for i in range(num_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
print(f"Generated password: {''.join(password)}")
