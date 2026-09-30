from collections import Counter
filename = input("enter file name: ")
with open (filename, "r") as file:
    text = file.read()

#count words
words = text.split()
count_word = Counter(words)

print("no of words:", count_word)