def shopping_cart(items):
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total
cart = [
    {'name': 'apple', 'price': 0.5, 'quantity': 4},
    {'name': 'banana', 'price': 0.3, 'quantity': 6},
    {'name': 'orange', 'price': 0.8, 'quantity': 3}
]   
print(shopping_cart(cart))