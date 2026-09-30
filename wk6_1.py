#Write a Python program that inputs two tuples and creates a third that contains all elements of the first followed by all elements of the second.

# t1 = tuple(input("Enter values for t1: ").split())
# t2 = tuple(input("Enter values for t2: ").split())

t1 = tuple(map(int, input("Enter values for t1: ").split()))
t2 = tuple(map(int, input("Enter values for t2: ").split()))

t3 = t1 + t2

print ("first tuple:", t1)
print ("second tuple:", t2)
print ("third tuple:", t3)
