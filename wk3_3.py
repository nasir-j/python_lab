# Write a program to print characters from a string which are present at even index
# numbers.
str = input("Enter a string:")
for i in range(0, len(str), 2):
    print (str[i], end = " ") 
    #Square brackets [] are used to access a character at a particular index.


text = "PYTHON"

for i in range(len(text)):
    if i % 2 == 0:
        print(text[i])