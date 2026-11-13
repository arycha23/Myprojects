vowels = ('a','e','i','o','u')
word = input("Enter a word: ")
number_of_vowels = 0

for letter in word:
    if letter.lower() in vowels:
        number_of_vowels += 1

print("Number of vowels = ", number_of_vowels)