# First, I will start defining the function convert_distance
# then, I will print the first part of the output which is a string "You Entered"
# then, I will assign variables for the numbers of miles, yards, feet, and inches by their respective relationships with the number of inches entered
    # for example, after counting the miles, the number of yards is the integer by dividing the remaining number of inches by 36, and so on
# after that, I will add several parallel conditional statements, asking the function to print the number of miles, yards, feet and inches ONLY IF they are not 0s.
    # please see the pseudo codes below that demonstrate the above
number of miles = d_inches // 63360
number of yards from the remainder after counting miles = (d_inches % 63360) // 36
number of feet from the remainder after counting miles and yards = ((d_inches % 63360) % 36) // 12
number of inches left from the remainder after counting miles, yards and feet = ((d_inches % 63360) % 36) % 12
if number of miles > 0 :
    print number of miles
if number of yards > 0 :
    print number of yards
if number of feet > 0 :
    print number of feet
if number of inches left > 0 :
    print number of inches 