# Write a program that inputs a main string and creates an encrypted string by embedding a short symbolbased string after each character. The program should also decrypt the string.
s = input("enter a string: ")
key = input("enter symbol string: ")
enc= ""
#encryption
for ch in s:
    enc = enc + ch + key
print("Encrypted string: ", enc)

#decryption
dec =""
for i in range (0, len(enc), len(key)+1):
    dec= dec + enc[i]

print("Decrypted String: ", dec)
