# Write a Python program to calculate the sum of squares of the first two digits and the last two digits of
# a 4-digit number, e.g., for 1233, calculate 12^2 + 33^2.

# n = input("Enter a 4 digit number: ")
# parts = [n[:2], n[2:]]

# for x in parts:
#     print(x)

# result = int(parts[0])**2 + int(parts[1])**2
# print(result)

# n = input("Enter a 4 digit number: ")

# x = ""
# y = ""

# for i in range(4):
#     if i < 2:
#         x = x + n[i]
#     else:
#         y = y + n[i]

# x = int(x)
# y = int(y)

# result = x**2 + y**2

# print(result)


#n = int(input("enter no: "))
n = input("Enter a 4-digit number: ")

if len(n) == 4 and n.isdigit():
    print("Valid 4-digit number:", n)

    ft = int(n) // 100
    lt = int(n) % 100

    result = ft**2 + lt**2
    print(result)

else:
    print("Please enter exactly 4 digits.")