def table(t):
        i = 1
        for row in t:
                print "%d." %i,
                for item in row:
                        print "%s\t" %item,
                print
                i += 1
logic = [
        ["True and False:", True and True],
        ["False and True:", False and True],
        ["1==1 and 2==1:", 1==1 and 2==1],
        ["\"test\" == \"test\":", "test" == "test"],
        ["1==1 or 2 != 1:", 1==1 or 2 != 1],
        ["True and 1==1:", True and 1==1],
        ["False and 0 != 0:", False and 0!=0],
        ["True or 1==1:", True or 1==1],
        ["\"test\" == \"testing\":", "test" == "testing"],
        ["1 != 0 and 2 == 1", 1!=0 and 2==1],
        ["\"test\" == 1", "test" == 1],
        ["not (True and False)", not (True and False)],
        ["not (1==1 and 0!=1)", not (1==1 and 0!=1)],
        ["not (10 == 1 or 1000 == 1000)", not (10 == 1 or 1000 == 1000)],
        ["not (1 != 10 or 3 == 4)", not (1 != 10 or 3 == 4)],
        ["not (\"testing\" == \"testing\" and \"Zed\" == \"Cool Guy\")", not ("testing" == "testing" and "Zed" == "Cool Guy")],
        ["1 == 1 and not (\"testing\" == 1 or 1 == 0)", 1 == 1 and not ("testing" == 1 or 1 == 0)],
        ["\"chunky\" == \"bacon\" and not (3 == 4 or 3 == 3)", "chunky" == "bacon" and not (3 == 4 or 3 == 3)],
        ["3 == 3 and not (\"testing\" == \"testing\" or \"Python\" == \"Fun\")", 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")]
        ]
table(logic)
