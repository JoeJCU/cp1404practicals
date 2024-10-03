MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsiusfahrenheit(celsius)
            print(f"{celsius} Celsius converts to {fahrenheit:.2f} Fahrenheit")

        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_celsius(fahrenheit)
            print(f"{fahrenheit} Fahrenheit converts to {celsius:.2f} Celsius")

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def celsiusfahrenheit(celsius):
    fahrenheit = (celsius * 9) / 5 + 32 #celsius to fah
    return fahrenheit

def fahrenheit_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32) #fah to celsius
    return celsius


main()
