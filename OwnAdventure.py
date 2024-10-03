print("==Choose your own adventure!==")

name = input("Enter your name: ")
print("Hello " + name + " welcome to my game.")

should_we_play = input("Do you want to play? ").lower()
if should_we_play == "yes" or should_we_play == "y":
    print("We gonna play!")
    weapon = input("Choose a  weapon. Axe/Sword? ").lower()

    directions = input("Do you want to go (right/left)? ").lower()
    if directions == "right":
        print("We went right.")
        swim_or_cross = input("In front of you there is a bridge. But also you could swim and get to the other end quicker. What option will you take?(Swim/Cross): ").lower()
        if swim_or_cross == "swim" and weapon == "axe":
            print("Surpise!!! There is a crocodile. Just take him out easily with the axe.You won!")
        elif swim_or_cross == "cross":
            print("You cross to the other side easily. No danger ahead of you.")
        else:
            print("That was a bad choice. Game Over!")

    elif directions == "left":
        print("We went left! Ahead of you is nothing but endless dark forest forest. Try again later. Game Over!")

    else:
        print("Sorry, not a valid reply, you die!")



else:
    print("We're NOT gonna play...")















