# Print the following pattern for the given number of rows.

# Assume N is always odd.

# Note : There is space after every star. Pattern for N = 7
# *
#  * *
#    * * *
#      * * * *
#    * * *
#  * *
# *

n = int(input())
for i in range(1, n//2+2):
    print(' '*(i-1),end="")
    print("* "*i,end=" ")
    print()
for i in range(n//2,0,-1):
    print(' '*(i-1),end="")
    print("* "*(i),end=" ")
    print()

