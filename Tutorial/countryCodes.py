country_codes = {1:"Usa", 91:"India", 36:"Australia", 44:"United Kingdom"}

i = int(input("Enter country code: "))

if i in country_codes:
    print("country is " + country_codes[i])
else:
    print("country code not found")