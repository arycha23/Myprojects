m = [0,1,0]
D = int(input("Enter number: "))

print(m)
for x in range(1, D):
    n = [0] * (len(m) + 1)

    for y in range(1, len(m)):
        n[y] = m[y-1] + m[y]
    print(n)
    m = n