VALID_PRODUCTS = ['hamburger', 'soda', 'hotdog']

def enter_order(customer_input):
    for product in VALID_PRODUCTS:
        if product in customer_input:
            return product
    return 'Product unavailable'

def greet_customer(customer_name):
    return f'Hello, {customer_name}'
    