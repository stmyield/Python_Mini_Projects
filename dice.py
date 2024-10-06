import random

def dice_roll():
    
    gaming = True
    while gaming:
        player = input("Do you want to roll? (Yes/No): ").lower()
        if player == "yes" or player == "y":
            dice = random.randint(1, 20)
            print(f"You rolled a {dice}.")

        else:
            print("Goodby!")
            break

dice_roll()