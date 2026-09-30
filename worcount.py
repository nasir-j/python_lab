"""
Word and Alphabet Counter
--------------------------
Reads a text file, counts occurrences of each word and each alphabet
(letter), and reports the letter with the maximum count.
"""

from collections import Counter
import string


def count_words_and_alphabets(filepath):
    word_counter = Counter()
    letter_counter = Counter()

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            # --- word counting ---
            # Split on whitespace, strip surrounding punctuation, lowercase
            words = line.split()
            for w in words:
                cleaned = w.strip(string.punctuation).lower()
                if cleaned:
                    word_counter[cleaned] += 1

            # --- alphabet (letter) counting ---
            for ch in line:
                if ch.isalpha():
                    letter_counter[ch.lower()] += 1

    return word_counter, letter_counter


def main():
    filepath = input("Enter path of the text file: ").strip()

    word_counts, letter_counts = count_words_and_alphabets(filepath)

    print("\n--- Word Counts ---")
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")

    print("\n--- Alphabet Counts ---")
    for letter, count in sorted(letter_counts.items()):
        print(f"{letter}: {count}")

    if letter_counts:
        max_letter, max_count = letter_counts.most_common(1)[0]
        print(f"\nAlphabet with maximum instances: '{max_letter}' ({max_count} times)")
    else:
        print("\nNo alphabets found in the file.")


if __name__ == "__main__":
    main()
