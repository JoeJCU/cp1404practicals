
numbers = []

def main():
    for i in range(5):
        user_input = int(input("Enter a number: "))
        numbers.append(user_input)

    for number in numbers:
        print(f"number: {number}")

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers)/len(numbers)}")



main()