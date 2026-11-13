# pizza cost $10
#ask how many pizzas user wants
#give total price


def pizza_to_price(num_of_pizza, cost_of_pizza):
    price = int(num_of_pizza) * int(cost_of_pizza)
    return f"{num_of_pizza} pizzas costs {price} dollars"

user_input = input("How many pizzas do you want: ")
value_input = int(user_input)

cost_of_pizza = input("How much pizza costs: ")
cost_input = int(cost_of_pizza)


value = pizza_to_price(value_input, cost_of_pizza)
print(value)







