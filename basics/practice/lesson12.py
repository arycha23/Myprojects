import array
arr = array.array('i', [1, 2, 3, 4, 5])
# Creating an array of integers
print(arr)
print("--------------------------")
########################################################################

arr = array.array('i', [1, 2, 3, 4, 5])
# Accessing elements by index
print(arr[0])
print(arr[2])
print("--------------------------")
########################################################################

arr = array.array('i', [1, 2, 3, 4, 5])
# Getting the length of the array
length = len(arr)
print(length)
print("--------------------------")

########################################################################

arr = array.array('i', [1, 2, 3, 4, 5])
# Looping through the array elements
for element in arr:
    print(element)
print("--------------------------")

########################################################################

arr = array.array('i', [1, 2, 3, 4, 5])
# Removing an element by value
arr.remove(3)
print(arr)
print("--------------------------")

########################################################################

arr = array.array('i', [1, 2, 3, 4, 5])
# Slicing the array
slice_arr = arr[1:4]
print(slice_arr)
print("--------------------------")

########################################################################

arr = array.array('i', [1, 2, 3, 4, 5])
# Searching for an element
index = arr.index(3)
print(index)
print("--------------------------")

########################################################################

arr = array.array('i', [1, 2, 3, 4, 5])
# Updating an element
arr[2] = 10
print(arr)