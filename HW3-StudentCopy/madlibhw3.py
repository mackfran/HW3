# Name: Mackenzie Francisco
# uniqname: mackfran
# Section Day/Time: Thursday/1-2PM
# References: Amanda McLeod, Colleen's MadLib generator code
#             Internet source (listed above the code)

# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

# Source:
	## http://www.nltk.org/book/ch05.html

import nltk
from nltk.book import *
import random
from nltk import word_tokenize,sent_tokenize

print("START*******")

# creates a list of the first 150 tokens from the text
tokens = text2[:150]
# prints the old text
print(" ".join(tokens), '\n')
# creates a list of tagged tuples
tagged_tokens = nltk.pos_tag(tokens)

# defines the 5 parts of speech to prompt for, including nouns
tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective","ADV":"an adverb"}
# sets what percent of the time each part of speech should be replaced
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1,"ADV":.1}

def spaced(word):
	# if the word is a punctuation mark, returns it
	if word in [",", ".", "?", "!", ":"]:
		return word
	# otherwise, returns the word with a space in front of it
	else:
		return " " + word

# creates an empty list for the words after replacement
final_words = []

# parses through the tagged list of tuples
for (word, tag) in tagged_tokens:
	# if the word is not a part of speech we're prompting for or
	# if replacing the word would exceed the probability of replacement for that word's part of speech,
	# adds the original word to the list
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	# otherwise, prompts user for a part of speech and adds that word to the list
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print("\n\nEND*******")
# prints the new text
print ("".join(final_words))