# NLP Text Preprocessing Engine (v2.2)

import string

# input text
text = input("Enter a paragraph: ")

# 1. convert to lowercase
text = text.lower()

# 2. remove punctuation
for char in string.punctuation:
    text = text.replace(char, "")

# 3. tokenize words
words = text.split()

# 4. count total words
word_count = len(words)

print("\nCleaned text:", text)
print("Tokens:", words)
print("Number of words:", word_count)

# 5. define stopwords (basic)
stopwords = ["is", "the", "and", "a", "an", "in", "on", "at", "to", "of"]

# 6. remove stopwords (keep important words like 'not')
filtered_words = []
for word in words:
    if word not in stopwords:
        filtered_words.append(word)

print("\nAfter removing stopwords:", filtered_words)

# 7. word frequency (on cleaned data)
frequency = {}
for word in filtered_words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequency (cleaned):")
for word, count in frequency.items():
    print(f"{word}: {count}")
