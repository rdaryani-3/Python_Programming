# character pattern

# Print the following pattern for the given N number of rows.

# Pattern for N = 4
# A
# BC
# CDE
# DEFG

x=65
n= int(input())

for i in range (1,n+1):
    for j in range(1,i+1):
        print(chr(x+i-1+j-1), end="")
    print()


# one =chr(x)
# print (chr(x+9))


