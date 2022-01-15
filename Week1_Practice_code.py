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
    game_answer = input("Do you want to play. Answer Y or N:")
    if game_answer == "Y":
        print("Great Choice " + name_answer + "lets play ")
    else:
        print("Never mind next time " + name_answer)
    return game_answer


name = ask_name()
play_game(name_answer=name)
