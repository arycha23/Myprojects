fruits = ["apple","orange", "apple","banana","grape","orange"]
fruitmap = {}
for fruit in fruits:
    if (fruitmap.get(fruit) == None):
        fruitmap[fruit] = 1
    else:
        fruitmap[fruit] = fruitmap[fruit] + 1

print(fruitmap)



