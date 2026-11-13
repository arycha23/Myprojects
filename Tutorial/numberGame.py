
import random
random_integer = random.randint(1, 10)


while (True):
    num = int(input("Enter number between 1 to 10: "))

    if num == random_integer:
        print("Match")
        break

    else:
        print("Try again")
