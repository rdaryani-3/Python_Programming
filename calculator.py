# calculator

# Write a program that performs the tasks of a simple calculator. The program should first take an integer as input and then based on that integer perform the task as given below. You should also take an integer n that would actually tell us how many times will the operations be performed.

# 1. If the input is 1, then 2 integers are taken from the user and their sum is printed.
# 2. If the input is 2, then 2 integers are taken from the user and their difference(1st number - 2nd number) is printed.
# 3. If the input is 3, then 2 integers are taken from the user and their product is printed.
# 4. If the input is 4, then 2 integers are taken from the user and the quotient obtained (on dividing 1st number by 2nd number) is printed.
# 5. If the input is 5, then 2 integers are taken from the user and their remainder(1st number mod 2nd number) is printed.
# 6. If the input is 6, then the program exits.
# 7. For any other input, then print "Invalid Operation".
x = 1
while x != 6:
    x = int(input())
    if x == 1:
        a = int(input())
        b = int(input())
        print(a+b)
    elif x==2:
        a = int(input())
        b = int(input())
        print(a-b)
    elif x==3:
        a = int(input())
        b = int(input())
        print(a*b)
    elif x==4:
        a = int(input())
        b = int(input())
        print(int(a/b))
    elif x==5:
        a = int(input())
        b = int(input())
        print(a%b)
    elif x==6:
        break
    else:
        print("Invalid Operation")