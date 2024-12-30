# sum even
# Given a number N, print sum of all even numbers from 1 to N.

sum = 0
n = int(input())
i = 1

# while (i <= n ):
#     sum = sum+i
#     i = i+1

for i in range(1,n+1):
    if i%2==0:
        sum = sum+i

print(sum)

