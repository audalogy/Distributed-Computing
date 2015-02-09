#Audrey Leung
#Password strength checker
#!/usr/bin/python2.7

import getpass

#prompt the user for a test password
def main():
	user_pass = getpass.getpass("Enter the secret password: ")
	if user_pass != "finish":
		#strength checker
		pass_strength(user_pass)
		# opens file and reads password without '\r\n'
		fo = open('common.passwords.sorted.txt','r')
		raw_pass = fo.readlines()
		clean_txt = [element.replace('\r\n', '') for element in raw_pass]
		#check that the password does not appear in a list of common passwords
		binary_search(user_pass,0,(len(clean_txt)-1),clean_txt,0)
		#start again
		# "The relationship between total comparisons and the size of the list is 
		# a max of approximately log base 2 of items in the list (10,000) or the 
		# number of times the list is divided by 2 before the function finds the password."
		print "Next Password!\n"
		main()
	elif user_pass == "finish":
		print "Ok, goodbye :("
		return

def pass_strength(user_pass):
	#count of conditions met
	conditions_met = 0
	#It has at least one uppercase and at least one lowercase letter
	Upper = False
	Lower = False
	user_pass_list = list(user_pass)
	for letter in user_pass_list:
		if letter.isupper():
			Upper = True
		if letter.islower():
			Lower = True 
	if not Upper or not Lower:
		print "Test: upper & lower case fail"
	elif Upper and Lower:
		print "Test: upper & lower case pass" 
		conditions_met += 1

	#It has at least one digit. isalpha() - returns true if all characters in the string are alphabetic and there is at least one character, false otherwise.
	Digit = False
	for letter in user_pass_list:
		if letter.isdigit():
			Digit = True
	if not Digit:
		print "Test: digits present fail"
	if Digit:
		print "Test: digits present pass"
		conditions_met += 1

	#t has at least one character that is a special character (not a letter or a digit). isalnum() - Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise.
	if user_pass == "":
		print "Test: special characters present fail"
	elif not user_pass.isalnum():
		print "Test: special characters present pass"
		conditions_met += 1
	elif user_pass.isalnum():
		print "Test: special characters present fail"

	#It has a length of at least six characters
	if len(user_pass) >= 6: 
		print "Test: six characters pass"
		conditions_met += 1
	if len(user_pass) < 6:
		print "Test: six characters fail"

	#Report strength of password
	if conditions_met == 0:
		print 'Password is "very weak."'
	if conditions_met == 1:
		print 'Password is "weak".'
	if conditions_met == 2:
		print 'Password is "medium strength".'
	if conditions_met == 3:
		print 'Password is "high medium strength".'
	if conditions_met == 4:
		print 'Password is "strong".'
	
#check that the password does not appear in a list of common passwords
def binary_search(user_pass,low_index,high_index,clean_txt,count):
	#increment count
	count += 1
	#turns user password into all lowercase
	lower_pass = user_pass.lower()

	#Base Case 1: if list has zero items, exit
	if len(clean_txt) == 0: 
		print 'No matches. Your password is NOT in the list.'	
		print 'Recursion called %d times.' % (count)
		return 

	#Base Case 2: if list has only one item (low_index = high_index) compare with user password
	if low_index == high_index:
		if lower_pass != clean_txt[low_index]:
			print 'No matches. Your password is NOT in the list.'
			print 'Recursion called %d times.' % (count)
		elif lower_pass == clean_txt[low_index]:
			print 'Password Match! You\'re in.'
			print 'Recursion called %d times.' % (count)
		return

	#Base Case 3: if list has 2 items remaining (even number of items), compare each with user password
	if low_index+1 == high_index: 
		if lower_pass != clean_txt[low_index] and lower_pass != clean_txt[high_index]:
			print 'No matches. Your password is NOT in the list.'
			print 'Recursion called %d times.' % (count)
		elif lower_pass == clean_txt[low_index] or lower_pass == clean_txt[high_index]:
			print 'Password Match! You\'re in.'
			print 'Recursion called %d times.' % (count)
		return	
		
	#recursive binary search
	mid_index = ((low_index+high_index)/2)
	mid_item = clean_txt[mid_index]
	if lower_pass == mid_item:
		print 'Password Match! You\'re in.'
		print 'Recursion called %d times.' % (count)
	#recursive on the first half of list
	elif lower_pass < mid_item: 
		high_index = mid_index
		binary_search(lower_pass,low_index,high_index,clean_txt,count)
	#recursive on the second half of list
	elif lower_pass > mid_item:
		low_index = mid_index
		binary_search(lower_pass,low_index,high_index,clean_txt,count)


if __name__ == "__main__":
	main()