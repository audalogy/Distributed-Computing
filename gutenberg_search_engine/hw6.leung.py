#Audrey Leung
#Gutenberg Search Engine 
#!~/usr/bin/python2.7

import re
import urllib 

def main():
	#open file and clean text. Create dictionary of books
	file_input = raw_input('Input text file of books: ')
	try:
		with open(file_input, "r") as f:
			#strip blank spaces /r/n and split book and URL by ','
			#make [[title,url],[title,url]]
			book_list = [line.strip().split(',') for line in f]
			#separate list into separate [title,url,title,url]
			sep_list = []
			for item in book_list:
				sep_list += item
			#add 0, 1, 2 to beginning of URL so it's [0, URL], [1, URL]...
			pattern = 'http'
			count = 0
			Title = []
			for item in sep_list:
				if re.match(pattern,item): #if item matches http in beginning
					loc = sep_list.index(item) #get index of item
					item_list = item.split()  #make item into a list
					item_list = [count] + item_list #prepend number to list
					sep_list[loc] = item_list #replace the indexed item with new list (with prepended numbers)
					count += 1
				else:
					item
					Title.append(item) #append titles to list Title
			#create dictionary Books with book titles as keys
			Books = dict([(k, v) for k,v in zip (sep_list[::2], sep_list[1::2])])
			# print 'BOOKS: ', Books
			# print "TITLE:", Title
	except IOError as (errno, strerror):
		print "I/O error({0}): {1}".format(errno, strerror)
		print "Check that file exists in correct directory referenced"
		main()
	while True:
		user_input = raw_input('Enter word search: ')
		query = user_input.lower()
		if query == "<terminate>":
			print "Ok, goodbye :("
			return
		elif query == '<catalog>':
			print Books
			main()
		elif query == '<titles>':
			print Title
			main()
		else: 
			search_engine(Books,Title,query)

def search_engine(Books,Title,query):
	#Create dictionary with query as the key index 	
	WordCounts = []
	Words = {}
	for key,value in sorted(Books.items(), key=lambda x: x[1]): #sort dictionary by value
		try:
			response = urllib.urlopen(value[1]) #open URL
			rfile = response.readlines() #read url
			clean_rfile = clean_text(rfile) #clean text_file	
			number = value[0]+1
			book_words = 0
			for word in clean_rfile: #search for word and increment
				if word == '' or word == ' ':
					book_words += 0
				elif word == query:
					book_words += 1
			WordCounts.append(book_words) #append word count in its place in the list for phase 2
			#Phase 3: if the word appears more than once in a book, print output
			if book_words > 0: 
				print number,'.','The word',query,'appears',book_words,'time(s) in', key,'(link:',value[1],')'
		except TypeError:
			print 'Wrong file type. Must be .txt file.'
			main()
		except IOError:
			print 'Broken URL.'
			main()
	
	#Phase 2 section commented out
	#Words[query] = WordCounts #set query as key and WordCounts as list
	#print 'Words[',query,'] = ',Words[query]

	if all(i==0 for i in WordCounts): #if word does not appear at all
		print 'The word %s does not appear in any books in the library.' % (query) 

def clean_text(rfile):
	str_list = [element.strip() for element in rfile]
	str_list = filter(None, str_list) #get rid of empty elements: ''
	#print str_list
	clean_list = []
	for line in str_list:
		word_list = line.split() #create new list called word_list containing line
		for word in word_list: 
			clean_word = "".join(l for l in word if l.isalpha()) #get rid of non-alphabetic characters
			lower_word = clean_word.lower() #make all lowercase
			#append to list
			clean_list.append(lower_word) #add words to list
	return clean_list

if __name__ == "__main__":
	main()