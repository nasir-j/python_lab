# Write a program to remove characters from a string starting from the nth position to
# the last and return a new string. Example: remove_chars("aligarh", 3) should output
# ali.
# def remove_chars(str, n):
#     return str[:n]
# str = input("Enter a string: ")
# n = int(input("Enter the position to remove characters from: "))
# print(remove_chars(str, n))

def rc(str,n):
    return str[:n]

str =input("enter a string:")
n= int(input("enter last postion to remove characters from:"))
result = rc(str,n)
print(result)