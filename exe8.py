'''It's result day at school and not everyone is happy. You decided to make your friends laugh by
 jumbling their names to come up with some funny names.
Your program should take the number of names and the names separated by space as input. Output
 should be funny names in the same order.
Input:
Enter number of friends:
3
Enter the name of your 3 friends:
Rohan Das
Shubham Agarwal
Ritesh Arora
Output:
Ritesh Das
Shubham Arora
Rohan Agarwal'''
import random
def jumble_name():
    fname = [name.split()[0] for name in namelist]
    lname = [name.split(" ",1)[1] for name in namelist]
    for _ in namelist:
        random_fname = random.choice(fname)
        random_lname = random.choice(lname)
        print(f"{random_fname} \"{random_lname}\"")



if __name__ == '__main__':
    number = int(input("Enter number of friend: "))
    namelist = []
    for i in range(number):
        namelist.append(input("Enter the name of your friend with surname: "))
    print(namelist)


    jumble_name()