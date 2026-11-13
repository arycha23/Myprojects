g = input("Gender (f or m): ")
a = int(input("age: "))


if (a >= 1 and a <= 12 and g == 'f'):
    print("you are a female child")

elif (a >= 1 and a <= 12 and g == 'm'):
    print("you are a male child")

elif(a >= 13 and a <= 18 and g =='f'):
    print("you are a female teen")

elif (a >= 13 and a <= 18 and g == 'm'):
    print("you are a male teen")

elif(a >= 19 and g == 'f'):
    print("you are a female adult")

elif(a >= 19 and g == 'm'):
    print("you are a male adult")
else:
    print("age is invalid")