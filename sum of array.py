# sum of array
# Given an array of length N, you need to find and print the sum of all elements of the array.

# Sample Input :
# 3
# 9 8 9
# Sample Output :
# 26
# print(sum)


n = int(input())

arr = list(map(int, input().split()))
sum=0
for i in arr:
    sum+=i

print(sum)



