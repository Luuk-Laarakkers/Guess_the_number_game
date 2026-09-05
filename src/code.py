
#Use random library
import random

#Maximum amount of tries to guess the number
max_tries = 10
#Maximum number (Guess a number under 100)
max_number = 100
#The solution is a random number
answer = random.randint (1, max_number)

#Gather a guess number from user
guess = int(input("Guess a number under 100: "))
tries = 0

while max_tries > 0:
    #Execute when guess == answer
    if guess == answer:
        #Loop executed 1 time, so tries + 1
        tries += 1
        print ("You guessed it! And that within", tries, "tries")
        #Break the rest of the loop, because number is found
        break
    else:
        #Loop executed 1 time, so tries + 1
        tries += 1
        #If answer is higher than guess, print "Higher"
        if guess < answer or guess <= 0:
            print ("Higher")
            #Ask the user for a new guess
            guess = int(input("Guess a number under 100: ")) 
        else:
            #If answer is lower than guess, print "Lower"
            if guess > answer or guess >= 0:
                print ("Lower")
                #Ask the user for a new guess
                guess = int(input("Guess a number under 100: "))
    #The loop executed 1 time (10 - 1 = 9 tries left)
    max_tries -= 1
if max_tries == 0:
    #If no tries are left, print:
    print ("Sadly, you did not guess the number correctly")

input("Press enter to exit...")
