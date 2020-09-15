import random
num = random.randint(1, 10)
def guess_number(num) :
    guess = int(input("Enter an integer between 1 and 10: "))
    while num != "guess":
        if guess < num:
            print ("guess is low")
            guess = int(input("Enter an integer between 1 and 10: "))
        elif guess > num:
            print ("guess is high")
            guess = int(input("Enter an integer between 1 and 10: "))
        else:
            print ("you are right")
            break
