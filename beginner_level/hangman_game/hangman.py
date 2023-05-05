from random import choice
from hangman_art import stages, words
import os
from time import sleep

chosen_word = [x for x in choice(words)]
underscores = ["_" for i in range(len(chosen_word))]
mistakes = 0
end_game = False

while not end_game:
    user_input = (input("Please, enter a letter\t")).lower()

    if user_input in underscores:
        print(f"You have already guessed {user_input}")

    if user_input in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == user_input:
                underscores[i] = user_input
                print(
                    f'You chose letter "{user_input}", it is in the word, your word looks like that:'
                )
                print("".join(underscores))
                print(f"Your status look like that:\n{stages[mistakes]}")
    else:
        mistakes += 1
        print(
            f'You chose letter "{user_input}", it is not in the word, your word looks like that:'
        )
        print("".join(underscores))
        print(f"Your status look like that:\n{stages[mistakes]}")

    sleep(2)
    os.system("clear")
    if mistakes == 6:
        print(f"Game over, the chosen word was {''.join(chosen_word)}")
        end_game = True
    if "_" not in underscores:
        print(f'Congratulations! You won! The word was : {"".join(chosen_word)}')
        end_game = True
