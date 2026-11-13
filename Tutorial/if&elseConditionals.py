
calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days):

    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days  * calculation_to_hours} {name_of_unit}"

    elif num_of_days == 0:
        return ("Enter valid positive number that is not 0")

    else:
        return ("Can't enter negative number")

def validate_and_exicute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        calculated_value = days_to_units(user_input_number)
        print(calculated_value)

    else:
        print("Please enter valid number")


user_input = input("Enter number of days to convert to hours!\n")
validate_and_exicute()

