h = int(input("Enter number: "))

for n in range(1, h+1):
    print("  "* (h-n), end='')
    for m in range(1, n+1):
        print(m, "  ", end=' ')

    print("")

for x in range(h-1, -1, -1):
    print("  "* (h-x), end='')
    for y in range(1, x+1):
        print(y, "  ", end=' ')

    print("")
