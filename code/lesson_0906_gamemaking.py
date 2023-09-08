import random


def frame_maker(msg:str, symbol:str, spaces:int)->str:
    height = 5
    width = 2+2*spaces+len(msg)
    cyan = "\33[0;36m"
    end_code = "\33[0m"

    top_line = symbol*width
    middle_line = symbol + (" "*(width-2)) + symbol
    msg_line = symbol + " "*spaces + msg.title() + " "*spaces + symbol
    banner = f"{top_line}\n{middle_line}\n{msg_line}{end_code}\n{middle_line}\n{top_line}"

    return banner


title = "Guess the Number"
cover_game = frame_maker(msg=title, symbol='*', spaces=9)
print(cover_game)


def pick_difficulty()->tuple:
    while True:
        difficulty = input("Choose a difficulty from Easy/Normal/Hard:  ").lower()
        if difficulty == 'easy' or difficulty == 'normal' or difficulty == 'hard':
            break
    if difficulty == 'easy':
        return random.randint(1, 50), 50
    elif difficulty == 'normal':
        return random.randint(1, 100), 100
    else:
        return random.randint(1,500), 500


difficulty = pick_difficulty()
higher_range = difficulty[1]
secret = difficulty[0]
count = 0

guess = int(input(f"Guess a number between 1-{higher_range}:  "))
while guess != secret:
    if guess > secret:
        print("Too high.")
    else:
        print("Too low.")

    guess = int(input(f"Guess a number between 1-{higher_range}:  "))
    count += 1
print(f"You won, it wook you {count} tries to get the number.")

