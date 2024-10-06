import random

def guess_num():

    gaming = True
    while gaming:
        player = int(input("Enter a number between 1 and 10: "))
        bot = random.randint(1, 10)

        if player < bot:
            print(f"Computer picked {bot}.")
            print(f"To low. Try again.")
        elif player > bot:
            print(f"Computer picked {bot}.")
            print(f"To high. Try again.")
        else:
            print(f"Computer picked {bot}.")
            print(f"Congrats! You guessed it.")
            break

guess_num()