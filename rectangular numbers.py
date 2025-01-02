# rectangular numbers

# Print the following pattern for the given number of rows.

# Pattern for N = 4
# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334  
# 4444444
# Input format : N (Total no. of rows)

# Output format : Pattern in N lines



n=int(input())
for i in range (2*n-1):
    for j in range (2*n-1):
        print(max(abs(n-1-i), abs(n-1-j))+1,end="")
    print()




