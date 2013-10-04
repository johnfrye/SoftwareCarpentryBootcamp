import sys
import string

# Grab the input
sentence_1 = sys.argv[1]
sentence_2 = sys.argv[2]

# one character in common, 
# sentence 1 has 1 unique character
# sentence 2 has 2 unique characters
#sentence_1 = "She sells seashells by the seashore."
#sentence_2 = "Someone yell out a sentence?"

alphabet = string.lowercase

sentence_1 = sentence_1.lower()
characters_1 = set(sentence_1)
letters_1 = characters_1.intersection(alphabet)
print letters_1

sentence_2 = sentence_2.lower()
characters_2 = set(sentence_2)
letters_2 = characters_2.intersection(alphabet)
print letters_2

common = letters_1.intersection(letters_2)

print len(common)
print len(letters_1) - len(common)
print len(letters_2) - len(common)


