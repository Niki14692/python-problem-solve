# code with harry problem 4
def palindrome(data):
    while True:
        if str(data) == str(data)[::-1]:
            print(f"Next palindrome is {data}")
            break
        else:
            data += 1


n = int(input("Enter the number of the test cases: "))
numbers = []
for i in range(n):
    num = int(input("Enter your test cases: "))
    numbers.append(num)

for i in numbers:
    palindrome(i)