# reverse number pattern

# Print the following pattern for the given N number of rows.

# Pattern for N = 4
# 1
# 21
# 321
# 4321


n= int(input())

for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j, end="")
    print()