fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])
print(fruits[2])
print(fruits[-1])
print(fruits[-2])
print("--------------------------")
############################################################################

fruits = ["apple", "banana", "cherry", "date"]
fruits.append("elderberry")
print(fruits)
print("--------------------------")
############################################################################

fruits = ["apple", "banana", "cherry", "date"]
fruits.remove("banana")
print(fruits)
print("--------------------------")
############################################################################

fruits = ["apple", "banana", "cherry", "date"]
fruits[1] = "blueberry"
print(fruits)
print("--------------------------")
############################################################################

print(fruits[1:3])
print(fruits[:2])
print(fruits[2:])
print(fruits[:])
print(fruits[::2])
print("--------------------------")
############################################################################

fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit)
