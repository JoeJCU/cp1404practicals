
numbers = []

def main():
    for i in range(5):
        user_input = int(input("Enter a number: "))
        numbers.append(user_input)

    for number in numbers:
        print(f"number: {number}")

    print(f"The first number is {numbers[0]}")



main()