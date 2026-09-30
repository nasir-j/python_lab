# Write a program to create a function cal_sum_sub() that accepts two variables and calculates addition and subtraction. Also, it must return both addition and subtraction in a single return call.
def cal_sum_sub(a,b):
    add = a+b
    sub = a-b
    return add, sub
n1= int(input("Enter first number:"))
n2= int(input("Enter second number:"))
print("Addition and Subtraction:", cal_sum_sub(n1,n2))
print("Addition:", cal_sum_sub(n1,n2)[0])
print("Subtraction:", cal_sum_sub(n1,n2)[1])