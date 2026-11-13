number = input("number: ")

len = len(number)
n = int(number) / pow(10,  (len-1))
n_text=""

match int(n):
    case 1: n_text = "one"
    case 2: n_text = "two"
    case 3: n_text = "three"
    case 4: n_text = "four"
    case 5: n_text = "five"
    case 6: n_text = "six"
    case 7: n_text = "seven"
    case 8: n_text = "eight"
    case 9: n_text = "nine"

print(n_text)




