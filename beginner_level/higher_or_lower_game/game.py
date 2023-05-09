import random 
from data import data
import os 


def new_data(data:list = data)->dict:
    return random.choice(data)

def delete(element:dict, data:list = data)->None:
    data.remove(element)
    return

def formula(dict1:dict, dict2:dict)->str:
    return f"A: {dict1['name']}, {dict1['description']} from {dict1['country']}\nOR\nB: {dict2['name']}, {dict2['description']} from {dict2['country']}"

def choose()->str:
    return input('What do you choose? "A" or "B"?').lower()

def winner(user_input:str,dict1:dict,dict2:dict)->str:
    win = dict1 if dict1['follower_count']>dict2['follower_count'] else dict2
    if win == dict1 and user_input == 'a':
        return True
    elif win == dict2 and user_input == 'b':
        return True
    else:
        return False

def game():
    print('Welcome to "Higher or lower" game!\n Your task is to choose who has more followers on social media')
    if input('Are you ready to start? ("yes")') == 'yes':

        game_on = True
        score = 0
        a = new_data()
        delete(a)
        while game_on:
            print(f'Your current score is {score}')
            b = new_data()
            delete(b)
            print(formula(a,b))
            user_input = choose()
            if winner(user_input,a,b):
                score += 1
                a = b
                os.system('clear')
                print('You have guessed correctly')
            else:
                os.system('clear')
                print(f'You lost. Your final score is {score} ')
                break

game()