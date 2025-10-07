# This code counts the number of times a word appears in a text

text = "Hello world. Welcome to the world of Python."
word = "world"
count = text.lower().split().count(word)
print(f"The word '{word}' appears {count} times.")