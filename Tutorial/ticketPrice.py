
age = int(input("Enter age: "))

if (age <= 12):
    print("Ticket price is $5 for children")

elif (age > 12 and age <= 18):
    print("Ticket price is $10 for teens")

elif (age > 18 and age <= 20):
    print("Ticket price is $20 for post-teen")

elif (age >= 60):
    print("Ticket price is $15 for seniors")

else:
    print("Normal ticket is $30")