# number pyramid

# Print the following pattern for a given n.

# For eg. N = 6
# 123456
#   23456
#     3456
#       456
#         56
#           6
#         56
#       456
#     3456
#   23456
# 123456


n = int(input())
for i in range(1, n+1):
    print(' '*(i-1),end="")
    for j in range (i, n+1):
        print(j,end="")
    print()
for i in range(n-1,0,-1):
    print(' '*(i-1),end="")
    for j in range (i,n+1):
        print(j,end="")
    print()
# for i in range(n//2,0,-1):
#     print(' '*(i-1),end="")
#     print("* "*(i),end=" ")
#     print()