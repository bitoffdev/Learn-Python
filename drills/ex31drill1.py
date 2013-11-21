prompts = [
    ["You enter a dark room with two doors.  Do you want to: (1) Go through the east door or (2) Go through the west door.", 2, 3], 
    ["You died."],
    ["You are in a room with a big green troll. Do you want to: (1) Attack him or (2)Go through the west door.", 1, 0],
    ["You are on a balcony. Do you want to: (1) Go inside or (2) jump off the balcony", 0, 1]
]

situation = 0

while situation != 1:
    print prompts[situation][0]
    choice = int(raw_input("> "))
    if choice==1:
        situation = prompts[situation][1]
    elif choice==2:
        situation = prompts[situation][2]
    else:
        print "You moron! That is not an option!"
    print "************************************************"
else:
    print "You moron! You died!"
