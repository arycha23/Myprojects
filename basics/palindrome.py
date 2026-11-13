word = "noon"
a = 0
b = len(word)-1
c = True

while(b>a):
    if(word[a] == word[b]):
        a = a + 1
        b = b - 1
    else:
        c = False
        break

if(c == True):
    print(word +" is palindrome")
else:
    print(word +" is not palindrome")
