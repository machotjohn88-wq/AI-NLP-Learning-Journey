
# NLP Text Preprocessing Engine (v1)

text = input("Enter a paragraph: ")

# convert to lowercase
text = text.lower()

# remove punctuation
import string
for char in string.punctuation:
    text = text.replace(char, "")

# tokenize words
words = text.split()

# count words
word_count = len(words)

print("\nCleaned text:", text)
print("Tokens:", words)
print("Number of words:", word_count)

# words frequency
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")