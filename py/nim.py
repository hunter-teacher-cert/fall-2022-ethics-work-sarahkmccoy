1
# nim.py
# Sarah McCoy
# CSCI 77800 Fall 2022
# collaborators: N/A
# consulted: K Herr

#import random
print("We're going to play the classic game of of Nim!\n")
# set initial number of stones
#Note, with the smart computer, it seems that as long as you go first, you can't win
n = 13
# set max number of the player can take
max_stones = 3
#Print(f Python): The f means Formatted string literals and it’s new in Python 3.6.
# The f or F in front of strings tells Python to look at the values inside {} and substitute them with the values of the variables if exist.  So you don't need type casting or string concatenation
print(f"There are {n} stones in the bag. When it's your turn, you can take from 1 to {max_stones} stones.")
print("The player who takes the last stone wins!\n")

#keep playing while there are stones left
while n > 0:
    print(f"There are {n} stones left.")
    player_takes = input("How many stones would you like to take?\n")
    # input validation: check if the input is a digit between 1 and max_stones but not more than n
    if not(player_takes.isdigit()):
        print(f"Invalid move. Please enter a whole number between 1 and {max_stones}.")
        continue #continue returns to top of while loop, while break exits the loop
    else:
        player_takes = int(player_takes)
        if player_takes < 1 or player_takes > max_stones:
            print(f"Invalid move. Please enter a whole number between 1 and {max_stones}.")
        	continue #why is this indentation a problem?
        elif player_takes > n:
            print(f"Invalid move. You can't take more stones than are left in the bag.")
            continue
    # calculate new bag total
    n -= player_takes
    print(f"There are {n} stones left.")
    # check for win
    if n == 0:
        print("You won! Congratulations!")
        break
    # # computer player move: attempt to get in winning position (multiple of max + 1)--this way player can't win
    # # if impossible, take one stone
    # elif n % (max_stones + 1) == 0:
    #     comp_move = 1
    # else:
    #     comp_move = n % (max_stones + 1)
        
    #  create situation where player can win to test player win scenario...right now player cannot win...
	else: #why is this indentation a problem?
		comp_move = random.randint(1,3)
   		print(f"The computer has taken {comp_move} stones.")
   		n -= comp_move
    # check for win
    	if n == 0:
			print("There are 0 stones left.\nComputer wins! Better luck next time.")
			break
