# Print the following pattern

# Pattern for N = 4

# *000*000*
# 0*00*00*0
# 00*0*0*00
# 000***000


n = int(input())
for i in range(1, n +1):
    print('0'*(i-1),end="")
    print("*",end="")
    print('0'*(n-i),end="")
    print("*",end="")
    print('0'*(n-i),end="")
    print("*",end="")
    print('0'*(i-1),end="")
    print()