fruits = ["apple","banana","mango"]
a=list()

for fruit in fruits:
    print(fruit +" "+ str(len(fruit)))
    a.append(len(fruit))

print(a)