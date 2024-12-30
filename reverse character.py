# reverse character

# Print the following pattern for the given number of rows.

# Pattern for N = 5
# E
# DE
# CDE
# BCDE
# ABCDE


x=65
n= int(input())

for i in range (1,n+1):
    for j in range(1,i+1):
        print(chr(x+n-1-i+j), end="")
    print()