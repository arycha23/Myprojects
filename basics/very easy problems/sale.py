#appept 3 items if total is >100 then 10% off
#total is 100-200 then 20% off
#>200 30% off
#if amount is <100 tell them how much is left to add their remaning value to get 100

item1 = int(input("Enter value of item 1: "))
item2 = int(input("Enter value of item 2: "))
item3 = int(input("Enter value of item 3: "))

value = item1 + item2 + item3

if(value == 100):
    value = value - (value * 0.1)
    print("new value is " + str(value) + " with 10% off")

elif(value > 100 and value<= 200):
    value = value - (value * 0.2)
    print("new value is " + str(value) + " with 20% off")

elif(value > 200):
    value = value - (value * 0.3)
    print ("new value is " + str(value) + " with 30% off")

else:
    remaining = 100 - value
    print("add $" + str(remaining) + " to get 10% off")

