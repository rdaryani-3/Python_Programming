# fibonacci

n = int(input())
curr = 1
prev = 0
count = 1
while count <= n:
    temp = curr 
    curr = prev + curr
    prev = temp
    count = count + 1
    
print(prev)