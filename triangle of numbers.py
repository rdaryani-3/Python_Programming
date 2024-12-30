# triangle of numbers

# Print the following pattern for the given number of rows.

# Pattern for N = 4


#             1
#            232
#           34543
#          4567654


n=int(input())
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1,i+1):
        print(i+j-1, end="")
    for k in range(1,i):
        print (2*i-k-1,end="")
    print()


