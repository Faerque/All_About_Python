# Finding Even and Odd Numbers
# count = 0
# for numbers in range(1, 10):
#     if numbers % 2 == 0:
#         count += 1
#         print(numbers)
# print(f"Here found {count} even numbers")

Even = 0
Odd = 0

for number in range(1, 10):
    if number % 2 == 0:
        Even += 1
        print(f"Even Number is {number}")
    elif number % 2 != 0:
        Odd += 1
        print(f"Odd Number is {number}")
    print(" ")
print(f"Here founded {Even} even numbers")
print(f"Here founded {Odd} odd numbers")