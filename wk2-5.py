#Write a program to find the sum of the digits of a supplied integer.

n= int(input("enter no"))
sum =0
while n>0:
    digit = n%10
    sum = sum + digit
    n=n//10
print(sum)
