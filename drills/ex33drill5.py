print '''
|===============================================|
|   With for loop and incrementer in the loop   |
|===============================================|
'''
numbers = []
for i in range(6):
    print "At the top i is %d" % i
    numbers.append(i)
    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
print "The numbers: "
for num in numbers:
    print num
print '''
|===============================================|
| With for loop without incrementer in the loop |
|===============================================|
'''
numbers = []
for i in range(6):
    print "At the top i is %d" % i
    numbers.append(i)
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
print "The numbers: "
for num in numbers:
    print num
