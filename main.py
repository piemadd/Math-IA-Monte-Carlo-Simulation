# Importing some libraries
import random as rand
import matplotlib as mpl
import matplotlib.pyplot as plt

# -------------------------

# Setup Variables

# Change these to change the basic operation functionality
# of the program as a whole. This will make the usage of 
# this program easier for people. I could prompt for these 
# values at the beginning of the program, but that would 
# cause too much hassle for people actually using the program
# when the same variables have to be processed multiple times,
# which would cause the same numbers to be inputted multiple
# times, which is annoying.

startingCash = 100000 # The starting amount of money of the player.
rounds = 1000 # The number of rounds which should be run.
bet = 100 # The amount of money which the player bets each round.

# -------------------------

# Function for printing the main menu. This is displayed
# when the program is initially run.

def mainMenu():
    print("Welcome to Piero's Monte Carlo Simulation!")
    print("This is for my IB Math SL Y2 IA, just to note.")
    print("")
    print("Technical specs for the project can be viewed in notes.txt and")
    print("the changelog is in changelog.txt. You may notice that is program")
    print("Is documented at a much higher extent than my other programs,")
    print("but that is just because this is an important grade for my math")
    print("class and I do not want to mess up on it.")
    print("")
    print("Note: The files saved from this program have a")
    print("Static naming system, so the files need to be renamed")
    print("every time the program is run. Also, the starting money")
    print("of the player, the rounds played, and the bet of the")
    print("player can be changed in the beginning of the python program.")
    print("")
    input("Press enter to continue and to start the program.")


# -------------------------

# Creating the Function which will roll the dice.
# We will roll two dice, and if the total number is between
# 1 and 5, the player wins. Otherwise, the "casino" will
# win. This function takes nothing in and returns a boolean 
# value; TRUE being the player winning, FALSE being the 
# casino winning.

def diceRoll():
    a = rand.randint(1,6)
    b = rand.randint(1,6)
    if ((a + b) < 6):
        return True
    else:
        return False

# -------------------------

# Creating the function which will figure out the amount of 
# money won or lost by the 'player' after each round. This function
# accepts the last known balance of the player, and returns what 
# there balance is after this round. This will allow for easier
# programming down the line when it comes to this repetetive task.

def figureWinnings(lastAmnt):
    global bet # Getting global variables
    won = diceRoll()
    if (won == True):
        finalAmnt = lastAmnt + bet
    else:
        finalAmnt = lastAmnt - bet
    return finalAmnt

# -------------------------

# Here we are plotting the final graph and then saving it to a 
# .png file for later usage in my IA. Also, this handily saves
# the array which is passed to it into a file by the name of
# plot.txt. Note: The naming system is static at this point,
# so file names WILL need to be changed inbetween the runnings
# of the program.

def plotGraph(final):
    plt.plot(final) # Plotting the array
    plt.savefig('plot.png') # Saving to image

    f = open("plot.txt","w+") # Creating the text file
    f.write(str(final)) # Saving the array to a file
    f.close() # Actually saving the file 

# -------------------------

# Here we are writing the actual loop. This look will run the 
# dice roll a certain amount of times until the desired number 
# rounds has occured.

final = [startingCash]
#final[0] = startingCash
x = 1
rounds = rounds + 1
while (x < rounds):
    final.append(figureWinnings(final[len(final) - 1]))
    print("Round number " + str(x) + " complete.")
    print("Total amount is now equal to " + str(final[len(final) - 1]))
    x = x + 1
plotGraph(final)

# -------------------------

# The entire basis of a monte carlo simulation is to simulate
# every possible outcome. This will require the advanced 
# graphing of numbers, which i have ***NO*** experience with
# when it comes to python. Wish me luck I guess???

# After some reading, plotting shouldn't be too difficult. 
# Still, when plotting a large number of lines, this will cause 
# "chugging" to occur. I plan on allowing for the data to be 
# outputted to some sort of number format, whether it is a CSV, 
# a JSON, or some other format, I am unsure of at this point. 

# Text Code for testing different functions. Will be removed 
#  in final program.
# x = 0
# while (x < 10):
#     print(diceRoll())
#     x = x + 1
# print(diceRoll())
#print(figureWinnings(10000))
#mainMenu()