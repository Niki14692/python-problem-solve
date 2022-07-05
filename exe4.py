# Problem Statement:- You are given a list that contains some numbers. You have to print a list of next palindromes
# only if the number is greater than 10; otherwise, you will print that number.
#
# Input:
# [1, 6, 87, 43]
#
# Output:
# [1, 6, 88, 44]

def palindrome(d):
    if d > 10:
        while True:
            if str(d) == str(d)[::-1]:
                print(f"next parindrome is {d}") 
                break  
            else:
                d += 1
            
    else:
        print(f"parindrome is {d}")
        
n = int(input("Enter the number of the test cases: "))
numbers = []
for i in range(n):
    num = int(input("Enter your test here: "))
    numbers.append(num)

for i in numbers:
    palindrome(i)
