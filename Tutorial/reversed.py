word = "hello"

arr = list(word)
flipped = len(arr)
arr_2 =[]

for x in range (len(arr)):
    arr_2.append(arr[flipped-1])
    flipped -= 1

print(arr_2)