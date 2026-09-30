# Write a Python program to create a dictionary with names and phone numbers; ask the user for a name and print the corresponding phone number.

dict = {
    "Nasir": "6205407095",
    "Nasar": "9905817966",
    "Naaz": "7360946684"
}

name = input("enter name: ")

print(dict.get(name, "not found"))