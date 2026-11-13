
a=[7,8,5,2,0,2]

odd=list()
even=list()

for x in a:
    if(x%2 == 0):
        odd.append(x)
    else:
        even.append(x)

print(even)
print(odd)