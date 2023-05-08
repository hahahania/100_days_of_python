import random


def win(num, attempts, type):
    if type == "easy":
        total = 10 - attempts
    else:
        total = 5 - attempts
    return (
        f"Congratulations the number was {num}, you have guessed it in {total} attempts"
    )


def result(num, player_num):
    if player_num < num:
        return f"Too low.\nGuess again"
    elif player_num > num:
        return f"Too high.\nGuess again"


def game():
    level = input(
        "Welcome to number guessing game!\n Do you want to try 'easy' or 'hard' level?\t"
    )
    if level == "hard":
        attempts = 5
    else:
        attempts = 10
    random_num = random.randint(1, 100)
    game_on = True
    while game_on:
        if attempts == 0:
            print(f"You lost, the number you were looking for was {random_num}")
        print(f"You have {attempts} attempts left")
        correct = False
        while not correct:
            try:
                player_num = int(input("Choose number from between 1 and 100 :\t"))
                correct = True
            except:
                print("Incorrect form, try again (number from 1 to 100)")
        if random_num == player_num:
            print(win(player_num, attempts, level))
            game_on = False
        else:
            print(result(random_num, player_num))
        attempts -= 1

    if input("Do you want to play again? (y/n)") == "y":
        game()


game()
