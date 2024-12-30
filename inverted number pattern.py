# inverted number pattern

# Print the following pattern for the given N number of rows.

# Pattern for N = 4
# 4444
# 333
# 22
# 1


n= int(input())

for i in range (n,0,-1):
    for j in range (1, i+1):
        print(i,end="")
    print()


