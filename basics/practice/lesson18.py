def greet(name):
    return f"Hello, {name}!"
message = greet("Alice")
print(message)

print("--------------------------------------")
######################################################################

my_list = [1, 2, 3, 4, 5]
print(len(my_list))

print("--------------------------------------")
######################################################################

def add_numbers(a, b):
    return a + b
result = add_numbers(3, 5)
print(result)

print("--------------------------------------")
######################################################################

add = lambda x, y: x + y
print(add(3, 5))

print("--------------------------------------")
######################################################################

def factorial(n):
    if n == 1:
        return 1

    else:
        return n * factorial(n - 1)
print(factorial(5))

print("--------------------------------------")
######################################################################

def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)

print("--------------------------------------")
######################################################################

def generate_numbers():
    for i in range(1, 6):
        yield i
for number in generate_numbers():
    print(number)