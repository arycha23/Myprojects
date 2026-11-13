word = "madam"
arr = list(word)
valid = False
a = 0
b= len(arr)- 1

while (b>a):
    if (arr[a] == arr[b]):
        valid = True
        a = a+ 1
        b = b- 1

    else:
        valid = False
        break

if valid == True:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
