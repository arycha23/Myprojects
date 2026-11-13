a = [5,8,3,7,2,4]

c=0
for x in range(0, len(a)):
    for y in range(x, len(a)):
        c= c+1
        if a[x] > a[y]:
            n = a[x]
            a[x]=a[y]
            a[y] = n
print(a)
print(c)