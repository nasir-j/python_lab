# # Write a Python program that defines is_special_number(n) to check if a number is divisible by 5, a palindrome, 
# # and has even digit sum. Between 100 and 999, print all special numbers and their count.

# def is_special_number(n):
#     if n%5 != 0:
#         return False

#     if str(n) != str(n)[::-1]:
#         return False

#     digit_sum = sum(int(d) for d in str (n))

#     if digit_sum %2 != 0:
#         return False

#     return True

# count = 0

# for n in range(100,1000):
#     if is_special_number(n):
#         print(n)
#         count = count +1

# print("Total special nos:", count)

def is_special_number(n):
    s = str(n)
    return (
        n % 5 == 0                            # divisible by 5
        and s == s[::-1]                      # palindrome
        and sum(int(d) for d in s) % 2 == 0   # even digit sum
    )
count = 0
for n in range(100,1000):
    if is_special_number(n):
        print(n)
        count = count +1

print("Total special nos:", count)

# special = [n for n in range(100, 1000) if is_special_number(n)]

# print("Special numbers:", *special)
# print("Count:", len(special))