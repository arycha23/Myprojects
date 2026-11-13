string = input("Enter a string: ")

words = string.split()

if words:
    print("Length of the last word:", len(words[-1]))
else:
    print("No words found")

