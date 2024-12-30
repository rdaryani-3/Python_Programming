# square pattern

# Print the following pattern for the given N number of rows.

# Pattern for N = 4
# 4444
# 4444
# 4444
# 4444


n = int(input())

for i in range (1,n+1):
    for j in range (1,n+1):
        print(n,end="")
    print()
