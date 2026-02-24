def temp_convert(value, unit):
    if unit == "C":
        return (value * 9/5) + 32
    elif unit == "F":
        return (value - 32) * 5/9
    else:
        return "Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit."
print(temp_convert(25, "C"))
print(temp_convert(77, "F"))
print(temp_convert(30, "X"))