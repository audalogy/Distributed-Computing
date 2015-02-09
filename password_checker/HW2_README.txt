Homework 2 is due at 9AM on 9/16.

In this assignment, you will write a password strength checker in Python.

Part (1)

In this part, you will prompt the user for a test password.  Check the password for the following conditions:

(a)  It has at least one uppercase and at least one lowercase letter
(b)  It has at least one digit
(c)  It has at least one character that is not a letter or a digit
(d)  It has a length of at least six characters

If exactly no conditions are met:  report that the password is "very weak"
If exactly one condition is met:  report that the password is "weak"
If exactly two conditions are met:  report that the password is "medium strength"
If exactly three conditions are met:  report that the password "high medium strength"
If all four conditions are met:  report that the password is "strong"

You should also output which conditions are met and not met.

The program should continue prompting the user for passwords until the user types "finish"

(Extra credit:  When the user types in his or her password, we want don't to display it on the screen.  Find a way in Python to display asterisks instead of the password)

Part (2)

In this part you will add a further check:  that the password does not appear in a list of common passwords.  We have procured a sorted list of common passwords common.txt.  The list is sorted.

First, change all capital letters in the users password to lower case letters.

You should use the binary search algorithm we discuss in class to search whether the user's password is on the list of common passwords or not.
 
Please output the total number of times your algorithm makes a comparison between the user's password and an entry on the list of common passwords. What is the relationship between this number and the size of the list?

(Extra credit:  convert your binary search to a recursive algorithm e.g., search(value, high_index, low_index).)

Please extensively test your assignment.  When it is complete, put it in a script named hw2.<lastname>.py.  Write a document (acceptable formats include pdf and text files) explaining how you tested your program (what test cases and strategies did you use) as hw2-test.<lastname>.txt or hw2-test.<lastname>.pdf.  Upload these files using the file upload tool available at https://www.ischool.berkeley.edu/uploader/?s=i206 Login with your I School userid and password and follow the directions there. If you wish to modify a file you have already submitted, you may do so by resubmitting it using the same tool. As long as it has the same filename, it will overwrite the existing file. We will mark the last file(s) submitted before the due date/time.

