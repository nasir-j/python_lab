#Write a program to calculate the cube of all numbers from 1 to a given number.

n = int(input("Enter a number: "))
for i in range (1,n):
    cube = i**3
    print("cube of", i, "is", cube)
