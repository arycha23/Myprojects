# accept coupon AAA for $5 off (use if else)

# Global variables
price = 10
discount = 0.05
code = "ABC"

#Function that takes intger and returns integer
def pizza_to_cost(num_of_pizzas) -> int:
    #local variables
    final_price = 0
    cost = num_of_pizzas * price

    if (num_of_pizzas >= 5):
        final_price = cost * (1 - discount)
    else:
        final_price = cost

    if(coupon == code):
        final_price = final_price - 5

    return final_price



user_input = input("Enter number of pizzas wanted: ")
user_input_number = int(user_input)

coupon = input("Enter coupon code: ")

pizza_price = pizza_to_cost(user_input_number)
print(pizza_price)


