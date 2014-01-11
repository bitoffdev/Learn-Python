#This program is modified from learnpythonthehardway.com exercise 6 by Elliot
#I add comments to help explain and understand this program

#This line inserts a number using the string modifier %d
x = "There are %d types of people." % 10
#This line creates a string variable named 'binary'
binary = "binary"
#This line creates a string variable named 'do_not'
do_not = "don't"
#This line inserts the two variables created in previous lines using string modifiers
y = "Those who know %s and those who %s." % (binary, do_not)

#These lines print variables x and y
print x
print y

#These lines print x and y into two variables using string modifiers
print "I said: %r." % x
print "I also said: '%s'." % y

#This line creates a boolean variable
hilarious = False
#This line creates a variable string with a unassigned string modifier in it
joke_evaluation = "Isn't that joke so funny?! %r"

#This line prints the string created in the last line and inserts the boolean variable hilarious
print joke_evaluation % hilarious

#These lines assign strings to two variables, w and e
w = "This is the left side of..."
e = "a string with a right side."

#this line combines to string variables
print w + e
