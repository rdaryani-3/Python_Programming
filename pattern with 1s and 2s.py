# pattern with 1s and 2s

# Problem statement
# Print the following pattern for the given N number of rows.

# Pattern for N = 4
# 1
# 11
# 121
# 1221

n= int(input())

for i in range (1,n+1):
    if i ==1:
        print("1",end="")
    else:
        for j in range(1,i+1):
            if j ==1 or j== i:
                print("1",end="")
            else:
                print("2",end="")
    print()