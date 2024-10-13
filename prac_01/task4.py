####Prac1 part 4/6

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
starValue = int(input("Enter a number: "))
for i in range(starValue):
    print('*', end=' ')
print()  # newline
# d
starValue = int(input("Enter a number: "))
for i in range(1, starValue + 1):  # starts at 1 and goes up depending on the value enetered
    for x in range(i):  # iterates as the i value increases. depending on the i value, * are printed
        print('*', end=' ')
    print()
