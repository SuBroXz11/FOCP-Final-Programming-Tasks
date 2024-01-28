# Function to check if the user input is positive integer and then return the input integer.
def positive_integer_input(prompt):
    '''Prompt the user to enter a positive integer.
    
    This function repeatedly asks user input until the user enters a value that is a positive integer.
    It checks if the value is non-negative and is a integer before returing the value.
    
    Parameter:
    promt(string): The prompt message displayed to the user.
    
    Returns:
    int: A positive integer entered by the user.
    '''
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and int(user_input) >= 0:
            return int(user_input)
        elif user_input.lstrip('-').isdigit():
            print("Please enter a positive integer!")
        else:
            print("Please enter a number!")

            
# Function to check if the user input is yes or no.
def yes_no_input(prompt):
    '''Prompt the user to enter 'Y' for yes and 'N' for no.
    
    This function repeatedly asks user input for 'Y' and 'N' until an appropriate response.
    The input is case-insensitive and is converted to uppercase to maintain consistency.
    
    Parameter:
    promt(string): The prompt message displayed to the user.
    
    Returns:
    str: A string entered by the user, either 'Y' or 'N'.
    '''
    while True:
        user_input = input(prompt).upper()
        if user_input in ["Y", "N"]:
            return user_input
        else:
            print('Please enter "Y" or "N".')
            
# Function to calculate the total price of pizza.
def calculate_total(total_pizzas, delivery, is_tuesday, app_used):
    '''Calculate the total price of pizzas based on user inputs.

    This function takes the number of pizzas, delivery option, Tuesday discount status,
    and app usage into account to determine the total price.

    Parameters:
    total_pizzas (int): The total number of pizzas ordered.
    delivery (str): "Y" if delivery is required, "N" otherwise.
    is_tuesday (str): "Y" if it's Tuesday, "N" otherwise.
    app_used (str): "Y" if the customer used the app, "N" otherwise.

    Returns:
    float: The total price of pizzas, considering all applicable discounts.
    '''
    pizza_price = 12
    delivery_cost = 2.50

    if total_pizzas >= 5 and delivery == "Y":
        delivery_cost = 0

    if is_tuesday == "Y":
        pizza_price *= 0.5

    pizzas_price = total_pizzas * pizza_price

    if delivery == "Y":
        total_price = pizzas_price + delivery_cost
    else:
        total_price = pizzas_price

    if app_used == "Y":
        total_price *= 0.75

    return total_price

# Program Header
print(f'''BPP Pizza Price Calculator
{"="*26}''')

# Main Program
# Get the number of pizzas the customer wants to order
total_pizzas = positive_integer_input("How many pizzas ordered? ")

# Ask whether the customer wants delivery service
delivery = yes_no_input("Is delivery required? ")

# Check if today is Tuesday for any special discount
is_tuesday = yes_no_input("Is it Tuesday? ")

# Ask if the customer used the mobile app for additional discount
use_app = yes_no_input("Did the customer use the app? ")

# Calculate the total price based on user inputs
total_price = calculate_total(total_pizzas, delivery, is_tuesday, use_app)

# Display the total price to the user
print(f'\nTotal Price: £{total_price:.2f}.')