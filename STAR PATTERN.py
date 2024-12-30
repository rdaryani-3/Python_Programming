# STAR PATTERN

# Problem statement
# Print the following pattern for the given N number of rows.

# Pattern for N = 4

#             *
#            ***
#           *****
#          *******

n=int(input())
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()