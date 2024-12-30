# number pattern 2 triangles

# Print the following pattern for n number of rows.

# Note: each line consist of equal number of characters + spaces. Suppose you are printing xth line for N=n. 
# You need to print 1..x followed by (n-x) spaces, again (n-x) spaces followed by x..1

# 12      21
# 123    321
# 1234  4321
# 1234554321

n = int(input())
for i in range(1, n +1):
    for j in range (1, i+1):
        print(j, end="")
    print(" "*2*(n-i),end="")
    for j in range (i, 0, -1):
        print(j,end="")
    print()