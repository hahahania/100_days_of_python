alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def coding(word:str, num:int, type:str):
    if type == 'decode':
        num *= -1
    new_word = ''
    for char in word:
        try:
            new_word += alphabet[alphabet.index(char)+num]
        except:
            index = alphabet.index(char)+num - len(alphabet)
            new_word += alphabet[index]
    return new_word
caeser_cipher=True

while caeser_cipher:
    type = input('Do you wanna encode or decode your message?\t')
    message = input('Type the message:\t').lower()
    num = int(input('Type the shift number:\t '))
    result = coding(message, num, type)
    print(f'\nThe result :\t {result}')
    decision = input('Do you want to continue encrypting/decrytping? (yes/no)').lower()
    if decision == 'no':
        caeser_cipher = False
