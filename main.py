import random
import math

#Select Your lower bond number and upper bond number
lower = int(input("Enter lower bond:--"))
upper = int(input("Enter upper bond:--"))

#It'll generate random number by random module,
#within the range of lower bond and upper bond 
x = random.randint(lower, upper)

#Calculating the minimum number of guessing
print("\n\tYou'hv only", round(math.log(upper - lower + 1, 2)),"chances to guess\n")

#It'll store chances of guess
count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1
    guess = int(input("Guess a number:--"))

    #Check number is Greater or Smaller or Equal
    if x == guess:
        print("\n\tCongratulations you did it in", count, "try\n")
        break
    elif x > guess:
        print("You guessed too low number , Try Again With higher number!")
    elif x < guess:
        print("You guessed too high number , Try Again With lower number!")

#If Guessing is more than required guesses, 
# shows this output.
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d"%x)
    print("\tBetter luck next time!\n")
