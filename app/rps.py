
import random
VALID_OPTIONS = ("rock", "paper", "scissors")

def determine_winner(u, c):
    if u == c:
        result = "TIE GAME"
    elif u == "rock" and c == "scissors":
        result = "USER WINS"
    elif u == "rock" and c == "paper":
        result = "COMP WINS"
    elif u == "scissors" and c == "rock":
        result = "COMP WINS"
    elif u == "scissors" and c == "paper":
        result = "USER WINS"
    elif u == "paper" and c == "rock":
        result = "USER WINS"
    elif u == "paper" and c == "scissors":
        result = "COMP WINS"
    return result


if __name__ == "__main__":

    print("Welcome to my game")

    player_choice = input("Please select an option ('rock', 'paper', 'scissors'): ")

    print("USER CHOSE:", player_choice)

    computer_choice = random.choice(VALID_OPTIONS)
    print("COMPUTER CHOSE:", computer_choice)


    result_message = determine_winner(player_choice, computer_choice)

    print(result_message)

