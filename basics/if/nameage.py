import datetime

# Single line comment
'''
 Multiline comments
 - accpeting input
 - converting to int, float, string
 - if, else if condition
 - boolean operation (boolean only has 2 values True/False)
 - comparison operators (==, !=, >=, >, =<, <)
 - logical operators (and, or)
'''

name = input("Enter Name: ")
yearborn = int(input("Enter Year born: "))
gender = input("Gender: ")
age = datetime.datetime.now().year-yearborn

if (gender == "f"):
    print(name+" is a "+str(age)+ " year old female" )
elif(gender =="m"):
    print(name+" is a "+str(age)+ " year old male")
else:
    print(name+" is a "+str(age)+ " year old unknown" )




