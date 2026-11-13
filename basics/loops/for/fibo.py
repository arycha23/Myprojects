
n= int(input("end number:"))

a=0
b=1
c=0

for x in range(0,n):
    c=a+b
    a=b
    b=c
print (c)
