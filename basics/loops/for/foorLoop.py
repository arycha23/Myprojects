n = int(input("End number for totalling : "))
total = 0

################### For loop
for x in range(0,n+1):
       total = total + x

print(total)

################### While loop
total = 0
while (n>=0):
       total = total + n
       n = n - 1
print(total)
