fahrenheit = float(input("Enter the temperature in Fahrenhit: "))

def fahrenhit_celcius(fahrenheit):
    return (fahrenheit - 32) / 5/9 # conversion to convert fahrenhit to celcius

celsius = fahrenhit_celcius(fahrenheit)
print(f"{fahrenheit} Fahrenheit converts to {celsius:.2f} Celsius")





celsius = float(input("Enter the temperature in Celsius: "))

def celcius_fahrenheit(celsius):
    return (celsius * 9.0) / 5 + 32

fahrenheit = celcius_fahrenheit(celsius)
print(f"{celsius} Celsius converts to {fahrenheit:.2f} Fahrenheit")