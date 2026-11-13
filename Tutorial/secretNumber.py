
numbers = [2,5,6,7,9]

for i in reversed(numbers):
    if i == numbers[0]:
        print("Secret number is ", i)
    else:
        print("Not secret number but number is ", i)