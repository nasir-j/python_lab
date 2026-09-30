# #Write a program to generate a 6-digit random secure OTP.

# import random
# otp = random.randint(100000, 999999)
# print("Your 6-digit OTP is:", otp)

# import secrets
# otp = secrets.randbelow(900000) + 100000
# print("Your 6-digit OTP is:", otp)

import random

otp = random.randint(100000, 999999)
print("Your OTP is: ", otp)