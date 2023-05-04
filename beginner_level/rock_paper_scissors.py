import random
ls = [0, 1, 2]
decision = {'rock': 0, 'paper': 1, 'scissors': 2}
drawings = {2: '''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \  
|___/\___|_|___/___/\___/|_|  |___/
''',
            1: ''' 
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|          ''',
            0: '''      
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\ 
                     '''}
player = decision[input("What do yoo choose? rock, paper or scissors?")]
computer = random.choice(ls)

if computer == player:
    print(f'You both chose {player}, its draw!')
    print(drawings[player])
elif (computer == 0 and player == 1) or (computer == 1 and player == 2) or (computer == 2 and player == 0):
    print(
        f'Player won!\n{drawings[player]}\nComputers decision:\n{drawings[computer]}')
else:
    print(
        f'Computer won!\n{drawings[computer]}\Players decision:\n{drawings[player]}')
