import re
from random import randint

def poem_maker(text_file1, text_file2):

	# output = open("text.txt", 'a')

	first = open(text_file1).read().rstrip('\r')
	#first = re.split('\W+', first)
	#first = [x.split(' ') for x in first.split('\n')]
	first = first.split(' ')

	second = open(text_file2).read().rstrip('\r')
	#second = re.split('\W+', second)
	#second = [x.split(' ') for x in second.split('\n')]
	second = second.split(' ')

	books = [first, second]
	whichbook = 0
	whichword = randint(0, len(first))
	currentbook = books[whichbook]
	currentword = currentbook[whichword]

	while True:
		currentword = currentbook[whichword]
		if '.' in currentword:
			whichword+=1
			break
		else:
			whichword+=1

	#CHANGE THE CRUX WORD
	word = ['and', 'or', 'but,']
	poem = str()
	while True:
		currentbook = books[whichbook]
		currentword = currentbook[whichword]
		if '.' in currentword:
			# print currentword,
			poem += currentword + " "
			#output.write(currentword + " ")
			break
		for g, group in enumerate(books):
			# Ignore the same list
			if group == currentbook:
				continue
			# If the currentWord is in a different list:
			if currentword in word:
				whichbook = g # switch lists to the new list
				whichword = group.index(currentword, randint(0, len(group))) # switch word index to word
		# print currentword,
		poem += currentword + " "
		#output.write(currentword + " ")
		whichword+=1
	return poem


