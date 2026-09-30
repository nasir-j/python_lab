# num = int(input("Enter number:"))

# original = num
# reverse = 0

# while num > 0:
#     remainder = num%10
#     reverse = reverse * 10 + remainder
#     num = num//10

# if original == reverse:
#     print("palindrome")
# else:
#     print("not palindrome")

# num = int (input("Enter number:"))
# if num == num[::-1]:
#     print("palindrome")
# else:   
#     print("not palindrome")

str = input("Enter a string: ")
rev = str[::-1]
print("reverse", rev)