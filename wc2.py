from collections import Counter

filepath = input("Enter file path: ")
text = open(filepath).read()

words = Counter(text.lower().split())
letters = Counter(c for c in text.lower() if c.isalpha())

print("Word counts:", dict(words))
print("Letter counts:", dict(letters))

max_letter = letters.most_common(1)[0]
print(f"Most frequent letter: '{max_letter[0]}' ({max_letter[1]} times)")
