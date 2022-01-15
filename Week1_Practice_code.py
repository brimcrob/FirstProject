"""
going to ask multipe choice questions
"""


def ask_name():
    name_answer = ""
    while name_answer == "":
        name_answer = input("What is your name? ")
    return name_answer


# ask if they want to play the game
def play_game(name_answer):
    game_answer = input("Do you want to play. Answer y or n:")
    if game_answer == "y":
        print("Great Choice " + name_answer + " lets play ")
    else:
        print("Never mind next time " + name_answer)
    return game_answer


def question_one(name_answer):
    q_1_answer = "Edinburgh"
    question1 = input("Q1: What is the capital of Scotland")
    if q_1_answer == "Edinburgh":
        print("Correct. Well done " + name_answer + "Keep going")
    else:
        print("Wrong. Better Luck next time" + name_answer)


name = ask_name()
play_game(name_answer=name)
question_one(name_answer=name)
