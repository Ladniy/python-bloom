import random


def is_human_win(human_hand: str, machine_hand: str):
    match human_hand:
        case "rock":
            if machine_hand == "scissors":
                return True
        case "paper":
            if machine_hand == "rock":
                return True
        case "scissors":
            if machine_hand == "paper":
                return True
        case _:
            return False


def main():
    print("Welcome to the Rock Paper Scissors game!")
    username: str = input("May i have your name? ")
    print("Hello, %s!" % username)
    print("Try to beat a machine!")

    for i in range(0, 3):
        hand_list: list = ["rock", "paper", "scissors"]
        machine_hand: str = random.choice(hand_list)
        user_hand: str = input("Rock, Paper or Scissors? ").lower()
        if user_hand == machine_hand:
            print("Draw!")
            continue
        game_status: str = "You win!" if is_human_win(user_hand, machine_hand) else "Machine win!"
        print(game_status)
        
if __name__ == '__main__':
    main()