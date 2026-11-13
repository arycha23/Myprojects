import random

while (True):
    random1 = random.randint(0, 100)
    random2 = random.randint(0, 200)

    if random1 == random2:
        print(f"matched {random1}  {random2}")
        break
    else:
        print(f"not matched {random1}  {random2}")