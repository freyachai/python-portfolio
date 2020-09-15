def convert_distance(d_inches) :
    # print the string that prompt the answer
    print ("You entered ")
    # assigning the variables representing the displays of miles, yards, feet, and inches left depending on their relationships with n_inches
    d_miles = d_inches // 63360
    d_yards = (d_inches % 63360) // 36
    d_feet = ((d_inches % 63360) % 36) // 12
    d_inches_left = ((d_inches % 63360) % 36) % 12
    # if the distance is larger than one mile, the below will output the mumber of miles
    if d_miles > 0 :
        print (d_miles, "miles")
    # after counting the number of miles, if the remaining distance is equal or larger than a yard, the below will output the number of yards
    if d_yards > 0 :
        print (d_yards , "yards")
    # after counting the number of yars, if the remaining distance is equal or larger than a foot, the below will output the number of feet
    if d_feet > 0 :
        print (d_feet, "feet")
    # after counting all the above, if there are any inches left, the below will output it
    if d_inches_left > 0 :
        print (d_inches_left, "inches")
