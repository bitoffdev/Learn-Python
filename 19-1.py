#This line defines a function called cheese_and_crackers with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #This line prints a string with the variable for the cheese count in it
    print "You have %d cheeses!" % cheese_count
    #This line prints a string with the variable for the number of boxes
    print "You have %d boxes of crackers!" % boxes_of_crackers
    The following lines just print more strings
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
#This line calls the function with ints for arguments
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
#These lines define variables for the amount of cheese and amount of boxes
amount_of_cheese = 10
amount_of_crackers = 50
#This line calls the function using the variables created above as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
#This line calls the function using math in the arguments
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
#This line calls the function using addition of variables in the arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
