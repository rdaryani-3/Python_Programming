# Print the following pattern for the given number of rows.

# Pattern for N = 4
# 1111
# 000
# 11
# 0

n= int(input())
for i in range (0,n):
    if i%2==0:
        print("1"*(n-i))
    else:
        print("0"*(n-i))
