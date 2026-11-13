
toll = 1.0 #constant
speed = int(input("Enter Speed: "))
passenger = int(input("Number of Passengers: "))

if (speed >= 60 and speed <= 65 and passenger <= 2):
    toll = toll + (toll * 0.1)
    print(toll)

elif (speed >= 65 and passenger <= 2):
    tool = toll + (toll * 0.2)
    print(toll)

elif (speed <= 60):
    print("Speed up")

else:
    print("No toll")