# nim.py
# Sarah McCoy
# CSCI 77800 Fall 2022
# collaborators: N/A
# consulted: K Herr

print("We're going to play the classic game of of Nim!\n")

# set initial number of stones
n = 12

# set max number of the player can take
max_stones = 3
#Print(f Python): The f means Formatted string literals and it’s new in Python 3.6.
# The f or F in front of strings tells Python to look at the values inside {} and substitute them with the values of the variables if exist.


print(f"There are {n} stones in the bag. When it's your turn, you can take from 1 to {max_stones} stones.")
print("The player who takes the last stone wins!\n")

while n > 0:
    print(f"There are {n} stones left.")
    player_takes = input("How many stones would you like to take?\n")

    # input check: check if the input is a digit between 1 and max_stones but not more than n
	# Python does has ! as not as well, need more info...
    if not(player_takes.isdigit()):
        print(f"Invalid move. Please enter a whole number between 1 and {max_stones}.")
      #"continue": if these any of these invalid conditions is met the while loop exits this iteration and goes back to the top of the while loop, ie, it doesn't subtract stones or check for win.  
			continue
    else:
        player_takes = int(player_takes)#cast input value as integer
        if player_takes < 1 or player_takes > max_stones:
            print(f"Invalid move. Please enter a whole number between 1 and {max_stones}.")
            continue
        elif player_takes > n:
            print(f"Invalid move. You can't take more stones than are left in the bag.")
            continue
    
    # if no invalid conditions exist, calculate new bag total
    n -= player_takes
    print(f"Now there are {n} stones left.")

    # check for win
    if n == 0:
        print("You win! Congratulations!")
        break # break exits the while loop and goes to next line outside it, rather than back to top of while loop.

    # smart computer player move: attempt to get in winning position (multiple of max + 1) (vs. random 1 - 3)
    # if impossible, take one stone
    elif n % (max_stones + 1) == 0:
        comp_move = 1
    else:
        comp_move = n % (max_stones + 1)
        
        # create situation where player can win to test player win scenario
        # comp_move = 1

    print(f"The computer has taken {comp_move} stones.")
    n -= comp_move
    
    # check for win
    if n == 0:
        print("There are 0 stones left.\nComputer wins! Better luck next time.")

