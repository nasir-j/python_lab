#Given a list of numbers, write a program to turn every item of the list into its square.

def list_sq(lst):

    return ([x**2 for x in lst])

n = int(input("enter the no of elements in the list: "))
lst =[]
for i in range(n):
    element = int(input("enter element {}:".format(i+1)))
    lst.append(element)

print("The squares of the numbers in the list are:", list_sq(lst))