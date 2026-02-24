def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(even_or_odd(34))
print(even_or_odd(27))
def add(a,b):
    return a+b
print(add(5, 7))
def subtract(a,b):
    return a-b  
print(subtract(10, 3))
def multiply(a,b):
    return a*b
print(multiply(4, 6))
def divide(a,b):
    if b != 0:
        return a/b
    else:
        return "Cannot divide by zero"
print(divide(10, 2))
print(divide(10, 0))
