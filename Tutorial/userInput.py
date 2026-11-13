calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days*calculation_to_hours} {name_of_unit}")

user_input = input("Enter number of days to convert to hours!\n")
print(user_input)
print("------------------------------------------------------------------------")



calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return(f"{num_of_days} days are {num_of_days*calculation_to_hours} {name_of_unit}")


my_var = days_to_units(20)
print(my_var)

