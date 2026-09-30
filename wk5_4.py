#Given two lists of numbers, write a program to create a new list containing odd numbers from the first list and even numbers from the second list.

n1 = int(input("Enter number of elements in first list: "))
list1 = []

for i in range(n1):
    x = int(input("Enter element: "))
    list1.append(x)

n2 = int(input("Enter number of elements in second list: "))
list2 = []

for i in range(n2):
    x = int(input("Enter element: "))
    list2.append(x)

new_list = []

for x in list1:
    if x % 2 != 0:
        new_list.append(x)

for x in list2:
    if x % 2 == 0:
        new_list.append(x)

print("New list:", new_list)
