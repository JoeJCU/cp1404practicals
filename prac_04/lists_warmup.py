numbers = [3, 1, 4, 1, 5, 9, 2]



# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] =
# numbers[3:4] = 1
# 5 in numbers
# 7 in numbers
# "3" in numbers
# numbers + [6, 5, 3] = adds 6,5 and 3 onto the numbers array

# 1) Change the first element of numbers to "ten" (the string, not the number 10)

numbers[0] = "ten"
print(numbers)

# 2) Change the last element of numbers to 1

numbers[-1] = 1
print(numbers)

# 3) Print all the elements from numbers except the first two (slice)

print(numbers[2:])

#Print whether 9 is an element of numbers

if 9 in numbers:
    print(f"9 is in numbers, {numbers}")
else:
    print(f"no 9 is in numbers, {numbers}")


