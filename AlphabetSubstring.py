"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

For problems such as these, do not include raw_input statements or define the variable s in any way. Our automated testing will provide a value of s for you - 
so the code you submit in the following box should assume s is already defined. 
If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set.

Note: This problem is fairly challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, 
we suggest that you move on to a different part of the course. 
If you have time, come back to this problem after you've had a break and cleared your head.
"""

#input
s = 'azcbobobegghakl'
#s = 'zyxwvutsrqponmlkjihgfedcba'
#s = 'gmsrehdm' #result is gms
#s = 'qgwhjkwkbmbdjlvlpe' #result is bdjlv
#s = 'mxfpfcnnubfslhmslpbihvkz' #result is cnnu
char_length = len(s)
#s = 'abcdbcd'

#function that determines the ranking of a given alphabet
def char_alpha_order(x):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	#alphabet = raw_input('Enter a string')
	return alphabet.index(x.lower())+1

#function that calculates the alphabetical distance of each character within a word in a list
#and return the word where its characters have smallest distance from each other
#and is not 
"""
def word_char_distance(x):
	word_averages = []
	for i in x:
		word_distance_total = 0
		#word_distance_average = 0
		prev_char_order = char_alpha_order(i[0])
		#print prev_char_order
		for s in i:
			char_distance = char_alpha_order(s) - prev_char_order
			#print s, char_alpha_order(s), char_distance
			word_distance_total += char_distance
			prev_char_order = char_alpha_order(s)
		word_distance_average = word_distance_total / len(i)
		
		#print i, len(i), word_distance_total, word_distance_average
		word_averages.append(word_distance_average)
	
	if sum(word_averages) == 0:
		return chunks[0]
	else: 
		best_word = word_averages.index(min(x for x in word_averages if x != 0))
		return chunks[best_word]
"""

#find word with the highest length in the list
def find_best_word(x):
	word_length = []
	for i in chunks:
		word_length.append(len(i))
	best_word = word_length.index(max(len(x) for x in chunks))
	#best_word = max(len(x) for x in chunks)
	#print best_word
	return chunks[best_word]


#variable to count the number of iterations based on the length of the string
iteration = 0

#variable to store the ranking of each alphabet, so differences between the ranking 
#of the previous and current alphabet can be established
prev_char_order = char_alpha_order(s[0])

#list to hold seperate words
chunks = []

#temporary location for the word being built
word = ''

for i in s:
	#keep a tab on the number of loops
	iteration += 1
	#if the current character's position is less than the previous then append the built word to the list,
	#clear the word and add current char to the newly created word
	if char_alpha_order(i) < prev_char_order:
		chunks.append(word)
		word = ''
		word += i
	#if the current character's position is not less than previous then keep appending to the same word
	else:
		word += i
		#if the current character is the last letter in the string then append to list and finish up the loop
		if iteration == char_length:
			chunks.append(word)
	
	#sets the global variable the position of the current character, so the next char in the loop can be
	#compared against this
	prev_char_order = char_alpha_order(i)

#print word_char_distance(chunks)
print find_best_word(chunks)
print chunks