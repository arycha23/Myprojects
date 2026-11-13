a = [1,2,8,9,5]
i = int(input("enter number: "))

for x in range(0, len(a)):
    for y in range(x+1, len(a)):
        if (a[x]+a[y] == i):
            print(a[x],a[y])