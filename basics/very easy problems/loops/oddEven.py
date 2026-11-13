
#loop 1-100
#take sum of all odd and even numbers

even=0
odd=0
for n in range(1,100):
    if(n%2 == 0):
        even = even + n
    else:
        odd = odd + n

print(odd)
print(even)

# array - fruits (multiples)
#find duplicates and list

fruits = ['apple','banana', 'grape', 'apple', 'banana']
duplicateFuits = {}

for f in fruits:
    if(duplicateFuits.__contains__(f)):
        c = duplicateFuits.get(f)
        c +=1
        duplicateFuits[f]=c
    else:
        duplicateFuits[f]=1

print (duplicateFuits)
