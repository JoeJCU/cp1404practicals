MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("fahrenheit: "))
        celsius = (fahrenheit - 32) / 1.8
        print(f"Result: {celsius:.2f} F")  # too two decimal places(:.2f)

        # TODO: Write this section to convert F to C and display the result
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.
        pass
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")




def fahrenhit_celcius(fahrenheit):
    return (fahrenheit - 32) / 5/9 # conversion to convert fahrenhit to celcius

celsius = fahrenhit_celcius(fahrenheit)
print(f"{fahrenheit} Fahrenheit converts to {celsius:.2f} Celsius")




def celcius_fahrenheit(celsius):
    return (celsius * 9.0) / 5 + 32

fahrenheit = celcius_fahrenheit(celsius)
print(f"{celsius} Celsius converts to {fahrenheit:.2f} Fahrenheit")