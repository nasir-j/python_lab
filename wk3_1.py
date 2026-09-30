#Write a program to print the following pattern using the for loop:
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1

rows = int(input("Enter the number of rows: "))
print("Number Pattern-->")

for i in range (rows, 0, -1):
    for j in range (i, 0, -1):
        print(j, end=" ")
    print()