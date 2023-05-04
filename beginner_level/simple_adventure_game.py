
print("Welcome to Treasure Island. Your mission is to find the treasure.")
direction = input('Do you wanto to go right or left?')

if direction == 'left':
    action = input('Do you wanna swim or wait for the boat?')
    if action == 'wait':
        door = input('Which door do you wanna choose? red, blue or yellow?')
        if door == 'red':
            print('Burned by fire. Game Over.')
        elif door == 'blue':
            print('Eaten by beasts. Game Over.')
        elif door == 'yellow':
            print('You win! Congratulations!')
        else:
            print('Game over')
    else:
        print('Attacked by trout. Game Over.')
else:
    print('Fall into a hole. Game Over.')
