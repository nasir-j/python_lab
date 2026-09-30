#2. Write a function to return True if the first and last number of a given list are the same. If the numbers are different, return False.
def list_fun(lst):
    if lst[0] == lst[-1]:
        return True
    else:
        return False

n = int(input("Enter the number of elements in the list: "))
lst = []
for i in range(n):
    element = int(input("Enter element {}: ".format(i+1)))
    #.format(i + 1) puts the value inside {}.
    lst.append(element)
    #append() adds the entered element to the list.
    
print("First and last numbers are the same:", list_fun(lst))
