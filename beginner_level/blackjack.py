import random 
names = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
value = {'Ace':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10}

class Player():
    def __init__(self,name:str):
        self.cards = []
        self.score = 0
        self.name = name

    def pick(self):
        new_card = random.choice(names)
        names.remove(new_card)
        self.cards.append(new_card)

    def count_points(self)->int:
        self.score = 0
        for card in self.cards:
            self.score += value[card]
        if 'Ace' in self.cards:
            if self.score >=21:
                self.score -= 10
        return self.score
    
    def failed(self)->bool:
        self.count_points()
        if self.score>21: 
            return True

    def show_cards(self)->str:
        return ", ".join(self.cards)
    
    def first_card(self)->str:
        return (self.cards[0]+'[]')
    
    
def check_winner(obj1:object, obj2:object)->str:
    obj1.count_points()
    obj2.count_points()
    if obj1.score>obj2.score:
        return obj1,obj2 
    else:
        return obj2,obj1


def game():
    name = input('Enter your name:\t')
    end = False
    player = Player(name)
    computer = Player('Dealer')

    for i in range(2):
        player.pick()
        computer.pick()
    print(f"Your cards are : {player.cards}\nYour current score is : {player.count_points()}\nDealer's cards are : {computer.first_card()}")

    if not player.failed() and not computer.failed():
        while not end:
            if input("Do you want to pick a new card or pass?('n' for new card, 'p' for pass)")=='n':
                player.pick()
                if not player.failed():
                    print(f'You win! Your score is : {player.score} Your score is : {player.score} and your cards are : {player.show_cards()}')
                    print(f"{computer.name}'s score is : {computer.score} and cards : {computer.show_cards()}")
                    end = True
                else: 
                    print(f'You lost :( Your score is : {player.score} and your cards are : {player.show_cards()}')
                    print(f"{computer.name}'s score is : {computer.score} and cards : {computer.show_cards()}")
                    end = True
            else:

                winner, loser = check_winner(player, computer)
 
                print(f"The winner is {winner.name}! The winner's score is {winner.score} and cards are : {winner.show_cards()}")
                print(f"The loser is {loser.name}! The loser's score is {loser.score} and cards are : {loser.show_cards()}")
                end = True
                
if __name__ == '__main__':
    if input('Do you want to play blackjack? (y/n)') == 'y':
        game()
    else:
        print('Hope to see you again! Bye!')