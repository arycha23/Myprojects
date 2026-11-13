x = int(input("Enter number: "))

for i in range(x,0,-1):
    for j in range(i,0,-1):
        print(str(j) + " " , end='')
    print()