from data import question_data


class Question:
    def __init__(self, data):
        self.data = data
        self.number = 0

    def __repr__(self) -> str:
        return f'The question is:\n{self.data[self.number]["text"]}'

    def answer(self):
        return self.data[self.number]["answer"]


class Player:
    def __init__(self):
        self.points = 0

    def answer(self, question):
        if input("Is it True or False?\t ") == question.answer():
            self.points += 1
            print(f"Your answer is correct, you have {self.points} points \n")
        else:
            print(f"Your answer is incorrect, you have {self.points} points \n")


game_on = True
question = Question(question_data)
player = Player()
while game_on:
    print(question)
    player.answer(question)
    question.number += 1
    if question.number == 12:
        game_on = False

print(f"You have finished quiz with score {player.points}. \n CONGRATULATIONS!")
