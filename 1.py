#print welcome message
#print("hello world")

#message = 'nasir\'s house'   #backslash 
#message = "nasir's house"    #double quotes
# message = """nasir's house     
# is far away
# from aligarh"""       #multiple lines
# print(len(message))
message = 'hello world'
print(message[0])  #prints first character
print(message[1])  #prints second character 
print(message[0:5])  #prints characters from index 0 to 4
print(message[:5])  #prints characters from index 0 to 4
print(message[2:5])  #prints characters from index 2 to 4
print(message.upper())
print(message.lower())
print(message.count('l'))  #counts number of occurrences of 'l'
print(message.find('world'))  #returns index of first occurrence of 'world' 
print (help(str.lower))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(-3))

x=10

if x % 2 == 0:
    print("even")
else:
    print("odd")

numbers = []

for i in range(20):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("Numbers divisible by 5:")

for num in numbers:
    if num % 5 == 0:
        print(num)


numbers = [10, 23, 45, 67, 80, 12, 15, 33, 50, 71,
           25, 19, 90, 42, 55, 61, 70, 88, 5, 31]

for num in numbers:
    if num % 5 == 0:
        print(num)


num = int(input("Enter number:"))

original = num
reverse = 0

while num > 0:
    remainder = num%10
    reverse = reverse * 10 + remainder
    num = num//10

if original == reverse:
    print("palindrome")
else:
    print("not palindrome")