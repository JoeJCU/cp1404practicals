totalPrice = 0
numItems = int(input("Number of items: "))
for i in range(numItems):
    priceItems = float(input("Price of item: $"))
    totalPrice += priceItems

if totalPrice > 100:
    totalPrice -= totalPrice * 0.10  # substracting the dicount value with the total price in one line
    print(
        f"Total price for {numItems} items is ${totalPrice:.2f}")  # {bonus:.2f} formates the output 'bonus' to 2 decimal places
