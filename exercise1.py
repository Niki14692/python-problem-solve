   
try:
    n = int(input("Enter number of apple: "))
    mn = int(input("Enter minimum number of student: "))
    mx = int(input("Enter maximum number of student: "))


    if mn > mx:
        print("You entered value of mn and mx is wrong, mn should be less than the mx!")

    for i in range(mn,mx+1):
        if mn == mx:
            print("This is not a range.")
        elif n % i == 0:
            print(f"{i} is a divisor of {n}")
        else:
            print(f"{i} is not a divisor of {n}")

except ValueError:
    print("Please Enter integer value ")
    exit()
    