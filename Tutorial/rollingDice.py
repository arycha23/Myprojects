import random

while (True):
    rolled = random.randint(1,7)
    roll_again = input("Do you want to roll? ")

    if (roll_again == "yes"):
        print("your rolled ", rolled)

    elif(roll_again == "no"):
        print("your rolled ", rolled)
        break
print("Thanks for playing!")