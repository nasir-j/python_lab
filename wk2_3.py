r1 = int(input("Enter start"))
r2 = int(input("Enter end"))

for num in range(r1, r2+1):
    if num > 1:
        for i in range (2,num):
            if num%i==0:
                break
        else:
            print(num)


# r1 = int(input("1st no:"))
# r2 = int(input("2st no:"))

# for num in range(r1 + r2+1):
#     if num > 1:
#         for i in range(2, num):
#             if num%i==0:
#                 break
#         else:
#             print(num)