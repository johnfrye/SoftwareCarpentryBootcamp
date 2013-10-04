import sys

# Get the list of words
words = sys.argv[1:]

# Sort the list
words.sort()

# Capitalize first letter
for i, w in enumerate(words):
	words[i] = w.capitalize()

# Extract the last word from the list
lastWord = words[-1]
words = words[:-1]

#print lastWord
#print words

# Join the words
sent = ", ".join(words) + " and " + lastWord + "."

print sent

