def celsius_to_others(c):
    f = (c * 9/5) + 32
    k = c + 273.15
    return f, k

def fahrenheit_to_others(f):
    c = (f - 32) * 5/9
    k = c + 273.15
    return c, k

def kelvin_to_others(k):
    c = k - 273.15
    f = (c * 9/5) + 32
    return c, f

# Taking user input
temp = float(input("Enter temperature value: "))
unit = input("Enter unit (C/F/K): ").upper()

# Conversion logic
if unit == "C":
    f, k = celsius_to_others(temp)
    print(f"Fahrenheit: {f:.2f} °F")
    print(f"Kelvin: {k:.2f} K")

elif unit == "F":
    c, k = fahrenheit_to_others(temp)
    print(f"Celsius: {c:.2f} °C")
    print(f"Kelvin: {k:.2f} K")

elif unit == "K":
    c, f = kelvin_to_others(temp)
    print(f"Celsius: {c:.2f} °C")
    print(f"Fahrenheit: {f:.2f} °F")

else:
    print("Invalid unit! Please enter C, F, or K.")
