#-*- coding: ascii -*-
import re
import nltk
from random import randint

# script, filename, b1, b2 = argv
# text_dir = os.path.join(os.getcwd(), "texts")
# fileyellow = "{}/{}".format(text_dir,"yellow.txt")
# filedickens = "{}/{}".format(text_dir,"DickensTaleofTwo.txt")

# filename = 'test.txt'
# output = open(filename, 'w')
def maker_of_poem(b1, b2):
	final_poem = str()
	first = open(b1).read().strip().replace('\r',' ').replace('\n', ' ')
	first = first.split(' ')
	first = filter(None, first)
	#first = re.split('\W+', first)
	#first = [x.split(' ') for x in first.split('\n')]

	second = open(b2).read().strip().replace('\r',' ').replace('\n', ' ')
	second = second.split(' ')
	second = filter(None, second)
	#second = re.split('\W+', second)
	#second = [x.split(' ') for x in second.split('\n')]

	conj = ['CC', 'IN', 'DT']
	verbs = ['VBZ', 'VBG', 'VBD', 'VBN', 'VBP']
	nouns = ['NN', 'NNS']
	sets = [conj, verbs, nouns]

	books = [first, second]
	whichbook = 0
	whichword = randint(0, len(first))
	currentbook = books[whichbook]
	currentword = currentbook[whichword]


	for x in xrange(0, 8):
		i = 0

		#selects a random point in the text and then finds the beginning of a sentence
		while True:
			currentword = currentbook[whichword]
			if '.' in currentword:
				whichword+=1
				break
			else:
				whichword+=1

		while True:
			currentbook = books[whichbook]
			currentword = currentbook[whichword]

			if '.' in currentword:
				final_poem += currentword + " " 
				# output.write(currentword + " ")
				break

			if i > 1:
				while True:
					if '.' in currentword:
						final_poem += currentword + " "
						# output.write(currentword + " ")
						break
					else:
						final_poem += currentword.replace(',', '\n').replace(':', '\n').replace('?', '\n').replace(';', '\n').replace('!', '\n').replace('--', '\n') + " " 
						# output.write(currentword.replace(',', '\n').replace(':', '\n').replace('?', '\n').replace(';', '\n').replace('!', '\n').replace('--', '\n') + " ")
						whichword+=1
						currentword = currentbook[whichword]
				break

			# text = unicode(nltk.word_tokenize(currentword),errors='ignore')
			text = nltk.word_tokenize(currentword)
			text = nltk.pos_tag(text)

			for g, group in enumerate(books):
				# Ignore the same list
				if group == currentbook:
					continue

				# If the currentWord is in a different list:
				if text[0][1] in verbs:
					# switch lists to the new list
					whichbook = g
					i+=1
					#output.write('\n')
					try:
						# switch word index to word
						whichword = group.index(currentword, randint(0, len(group))) 
					except:
						whichword = group.index("and", randint(0, len(group)-100))
			
			final_poem += currentword.replace(',', '\n').replace(':', '\n').replace('?', '\n').replace(';', '\n').replace('!', '\n').replace('--', '\n') + " " 
			# output.write(currentword.replace(',', '\n').replace(':', '\n').replace('?', '\n').replace(';', '\n').replace('!', '\n').replace('--', '\n') + " ")
			whichword+=1
		final_poem += '\n'
		# output.write('\n')
	final_poem += '\n'
	# output.write('\n')
	return final_poem

# print(maker_of_poem(fileyellow,filedickens))

