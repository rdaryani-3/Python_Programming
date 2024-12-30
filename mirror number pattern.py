# mirror number pattern
# Problem statement
# Print the following pattern for the given N number of rows.

# Pattern for N = 4

# ...1
# ..12
# .123
# 1234




# The dots represent spaces.




n= int(input())

#METHOD-1  ---------------------------------

for i in range (n,0,-1):
    for j in range (1, i):
        print(" ",end="")
    for k in range (1,n-i+2):
        print(k,end="")
    print()


 #METHOD-2  ---------------------------------   

for i in range(1, n + 1):
    # Print leading spaces
    print(" " * (n - i), end="")
    # Print numbers
    for j in range(1, i + 1):
        print(j, end="")
    print()