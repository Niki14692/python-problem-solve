'''
Python Practice problem 8 (Easy, 10 points)
Rohan Das Is A Fraud
Rohan das is a fraud by nature.
Rohan Das wrote a python function to print a multiplication table of a given number and put one of the values (randomly generated) as wrong.
Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this! 
So you decided to use your python skills to counter Rohan’s actions by writing a python program that validates Rohan’s multiplication table.
Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.
Note: Rohan’s function returns a list of numbers like this
Rohan Das’s Function Input:
rohanMultiplication(6)
Rohan’s function returns this output:
[6, 12, 18, 26, …., 60]
You have to write a function isCorrect(table, number) and return the index where rohan’s function is wrong and print it to the screen! If the table is correct, your function returns None.
'''
import random
def rohanmultiplication(number):
    wrong = random.randint(0, 9)
    table = [i * number for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(0, 10)
    return table

def iscorrect(table, number):
    for i in range(1, 11):
        if table[i-1] != i * number:
            return i 
    return None

if __name__ == "__main__":
    number = int(input("Enter the number: "))
    mytable = rohanmultiplication(number)
    print(mytable)
    wrongindex = iscorrect(mytable, number)
    print(f"The table is wrong at index {wrongindex}")



print(-8//3)