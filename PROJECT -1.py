                                            #SNAKE,WATER,AND GUN



import random

while True:
    you = input("Enter s for Snake, w for Water, g for Gun (q to quit): ").lower()

    if you == "q":
        break

    if you not in ["s", "w", "g"]:
        print("Invalid input!")
        continue

    computer = random.choice(["s", "w", "g"])

    print("You chose:", you)
    print("Computer chose:", computer)

    if you == computer:
        print("Draw!")
    elif you == "s" and computer == "w":
        print("You win!")
    elif you == "w" and computer == "g":
        print("You win!")
    elif you == "g" and computer == "s":
        print("You win!")
    elif you == "w" and computer == "s":
        print("You lose!")
    elif you == "g" and computer == "w":
        print("You lose!")
    elif you == "s" and computer == "g":
        print("You lose!")

print("Game over!")

