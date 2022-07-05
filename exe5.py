# Problem Statement:- Generate a random integer from a to b. You and your friend have to guess a number between two
# numbers a and b. a and b are inputs taken from the user. Your friend is player 1 and plays first. He will have to
# keep choosing the number and your program must tell whether the number is greater than the actual number or less
# than the actual number. Log the number of trials it took your friend to arrive at the number. You play the same
# game and then the person with minimum number of trials wins! Randomly generate a number after taking a and b as
# input and don’t show that to the user.
#
# Input:
# Enter the value of a
# 4
# Enter the value of b
# 13
# Output:
# Player1 :
# Please guess the number between 4 and 13
# 5
# Wrong guess a greater number again
# 8
# Wrong guess a smaller number again
# 6
# Correct you took 3 trials to guess the number
# Player 2:
#
# Correct you took 7 trials to guess the number
# Player 1 wins!
from pickletools import read_unicodestring1
import random  
 
a = int(input("Enter the minimum value of the a: "))
b = int(input("Enter the maximum value of the b: "))
count_1 = 0
count_2 = 0

rnd = random.randint(a,b)
numoftry_1= 1
while(numoftry_1<7):
    
    # player 1 guess the number
    guess_1 = int(input(f"Player_1:Please guess the number between {a} and {b}.\n"))
    count_1 = count_1 + 1
    if guess_1 == rnd:
        print(f"Correct you took {count_1} trials to guess the number")
    elif guess_1 > rnd:
        print("opps!!Wrong guess....guess a smaller number again")
    else:
        print("opps!!Wrong guess....guess a greater number again")
        break
rnd1 = random.randint(a,b)
numoftry_2= 1
while(numoftry_2>7):
    
    guess_2 = int(input(f"Player_2:Please guess the number between {a} and {b}.\n"))
    count_2 = count_2 + 1
    if guess_2 == read_unicodestring1:
        print(f"Correct you took {count_2} trials to guess the number")
    elif guess_2 > rnd1:
        print("opps!!Wrong guess....guess a smaller number again")
    else:
        print("opps!!Wrong guess....guess a greater number again")
        break

if count_1 < count_2:
    print("player_1 win the game!")
else:
    print("player_2 win the game!")
