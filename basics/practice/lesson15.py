# Creating a tuple with multiple items
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print("--------------------------")
############################################################################

# Creating a tuple with one item
single_item_tuple = (5,)
print(single_item_tuple)
print("--------------------------")
############################################################################

# Creating an empty tuple using the tuple() constructor
empty_tuple = tuple()
print(empty_tuple)
print("--------------------------")
############################################################################

# Creating a tuple from a list
my_list = [1, 2, 3, 4, 5]
tuple_from_list = tuple(my_list)
print(tuple_from_list)
print("--------------------------")
############################################################################

# Creating a tuple from a string
my_string = "hello"
tuple_from_string = tuple(my_string)
print(tuple_from_string)
print("--------------------------")
############################################################################

# Creating a tuple from another tuple
original_tuple = (1, 2, 3)
new_tuple = tuple(original_tuple)
print(new_tuple)
print("--------------------------")
############################################################################

# Creating a tuple with one item using a list
single_item_list = [5]
single_item_tuple = tuple(single_item_list)
print(single_item_tuple)