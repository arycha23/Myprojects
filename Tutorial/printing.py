print("20 days are "+ str(20*24*60)+ " minutes")

print(f"20 days are {20*24*60} minutes")
print(f"35 days are {35*24*60} minutes")
print(f"50 days are {50*24*60} minutes")
print(f"110 days are {110*24*60} minutes")
print("---------------------------------------")


print(f"20 days are {20*24*60*60} seconds")
print(f"35 days are {35*24*60*60} seconds")
print(f"50 days are {50*24*60*60} seconds")
print(f"110 days are {110*24*60*60} seconds")
print("---------------------------------------")


calculation_to_units = 24*60*60
name_of_unit = "seconds"

print(f"20 days are {20*calculation_to_units} {name_of_unit}")
print(f"35 days are {35*calculation_to_units} {name_of_unit}")
print(f"50 days are {50*calculation_to_units} {name_of_unit}")
print(f"110 days are {110*calculation_to_units} {name_of_unit}")
print("---------------------------------------")


calculation_to_units = 24
name_of_unit = "hours"

print(f"20 days are {20*calculation_to_units} {name_of_unit}")
print(f"35 days are {35*calculation_to_units} {name_of_unit}")
print(f"50 days are {50*calculation_to_units} {name_of_unit}")
print(f"110 days are {110*calculation_to_units} {name_of_unit}")
print("---------------------------------------")


calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days*calculation_to_hours} {name_of_unit}")
    print(custom_message)


days_to_units(20, "Awesome!")
days_to_units(35,"Looks Good!" )
days_to_units(50,"Great!")
days_to_units(110,"Nice")