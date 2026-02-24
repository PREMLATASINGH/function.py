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
def greet(name="Guest"):
    return f"hello, {name} welcome to india!"

print(greet("Adwik"))
print(greet("uday"))
print(greet())
def print_numbers(*args):
    return args
print(print_numbers(1, 2, 3, 4, 5,"prema"))
def sum_numbers(*args):
    return sum(args)    
print(sum_numbers(1, 2, 3, 4, 5))