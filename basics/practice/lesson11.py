###Break Statement:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number == 5:
        break
    print(number)
print("Loop terminated when number reached:", number)
print("")
#######################################################################
###Continue Statement:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        continue
    print(number)
print("Loop skipped even numbers")
print("")
#######################################################################
###The Range Function:

for i in range(1, 10, 2):
    print(i)
print("")
#######################################################################
###Else in for loop:

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number % 7 == 0:
        print(f"Found a multiple of 7: {number}")
        break
else:
    print("No multiples of 7 found in the list")
