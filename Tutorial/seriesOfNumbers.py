
user = input("Enter Username: ")
pas =  input("Enter Password: ")

username = "admin"
password = str(1234)

if (username == user and password == pas):
    print("Access granted")

elif (username == user and password != pas):
    print("Incorrect password")

else:
    print("Unknown user")