# Print the following pattern for the given N number of rows.

# Pattern for N = 4
# 1
# 11
# 202
# 3003

n= int(input())

for i in range (1,n+1):
    if i ==1:
        print("1",end="")
    else:
        for j in range(1,i+1):
            if j ==1 or j== i:
                print(i-1,end="")
            else:
                print("0",end="")
    print()