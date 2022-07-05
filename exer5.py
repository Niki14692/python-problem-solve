import random


def guess_game(a, b, actual):
    guess = int(input("guess the number between {a} and {b}\n"))
    nguess = 1
    while guess != actual:
        if guess > actual:
            guess = int(input("opps!!Wrong guess....guess a smaller number again\n"))
            nguess += 1

        else:
            guess = int(input("opps!!Wrong guess....guess a greater number again\n"))
            nguess += 1

    print(f"you guessed the number in {nguess} guesses\n")
    return nguess






if __name__ == "__main__":
    a = int(input("Enter the value of a\n"))
    b = int(input("Enter the value of b\n"))
    print("player 1's turn")
    actual1 = random.randint(a, b)
    g1 = guess_game(a, b, actual1)

    print("player 2's turn")
    actual2 = random.randint(a, b)
    g2 = guess_game(a, b, actual2)

    if g1 > g2:
        print("Player 2 won the match!\n")

    elif g1 < g2:
        print("Player 1 won the match!\n")

    else:
        print("Its a Tie!\n")

