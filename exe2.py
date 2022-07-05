print("Enter the numbers of the list one by one\n")
size = int(input("Enter the size of list "))
mylist = []
for i in range(size):
    mylist.append(int(input("Enter list element: ")))
print(f"your list is here {mylist}")

# method one
a = mylist[:]
a.reverse()
print(f"My First reveresed list of {mylist} is {a}")

# method two
b = mylist[::-1]
print(f"My Second reveresed list of {mylist} is {b}")

# method three
c = mylist[:]
for i in range(len(c)//2):
    c[i], c[len(c) -i -1] = c[len(c) -i -1], c[i]
print(f"My Third reveresed list of {mylist} is {c}")