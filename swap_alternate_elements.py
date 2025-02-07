def swapAlternate(arr, n) :
    #write your code here 
    temp=0;
    for i in range(0,n-1,2):
       temp=arr[i] 
       arr[i]=arr[i+1]
       arr[i+1]=temp
    

t=int(input())
for x in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]
    swapAlternate(arr,n)
    for i in range(n):
        print(arr[i], end=" ")
    print()


# print(arr)
