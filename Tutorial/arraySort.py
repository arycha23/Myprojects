a = [8,2,5,4,3]
total = 0

for x in range(0,len(a)):
    total = a[x] + total

if (total % 2 == 1):
    print("Even")
else:
    print("Odd")