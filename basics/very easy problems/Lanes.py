import random

while(True):
    number = random.randint(1,4)
    lane = int(input("Enter lane number: "))

    if (number == lane):
        print ("Go")
        break
    else:
        print ("wait")