#Write a program to generate a random password that is 10 characters long, with at least 2 uppercase letters, 1 digit, and 1 special symbol.

import secrets
import string

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
special = "!@#$%^&*"

password = [
    secrets.choice(uppercase),
    secrets.choice(lowercase),
    secrets.choice(digits),
    secrets.choice(special)
]

all_characters = uppercase + lowercase + digits + special

for i in range(6):
    password.append(secrets.choice(all_characters))

secrets.SystemRandom().shuffle(password)

password = "".join(password)

print("Random password:", password)