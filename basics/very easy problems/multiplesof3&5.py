#find multiples of 3 & 5    Use mudulo (for remainder) & if condition in loop

n = int(input("Enter a number : "))

for number in range(0,n):
    if (number%3==0):
        print (str(number) + " multiple of 3")

    elif (number%5==0):
        print (str(number) + " multiple of 5")
