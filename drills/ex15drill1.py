#This line imports the arguments given to the program at start using sys module
from sys import argv

#This line puts argv values into two variables
script, filename = argv

#This line opens the file given to the program using argv
txt = open(filename)

#This line outputs the argv filename input
print "Here's your file %r:" % filename
#This line prints the file
print txt.read()

#The following lines do the same thing without using argv:
print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()
