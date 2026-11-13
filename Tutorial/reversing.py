word = "hello"
arr = list(word)

a = 0
b = len(arr) - 1
c = 0

while (b > a):
    c = arr[a]
    arr[a] = arr[b]
    arr[b] = c

    a = a + 1
    b = b - 1
    break

print(arr)