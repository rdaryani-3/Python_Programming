# pyramid number pattern
# Print the following pattern for the given number of rows.

# Pattern for N = 4
#    1
#   212
#  32123
# 4321234




n = int(input())
for i in range(1, n +1):
    print(' '*(n-i),end="")
    for j in range (i,1,-1):
        print(j,end="")
    for j in range (1,i+1):
        print(j,end="")
    print()