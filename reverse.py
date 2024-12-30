# reverse of a number
# Write a program to generate the reverse of a given number N. Print the corresponding reverse number.

# Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.

#Method-1 through string


def reverse(n):
    res=0
    while(n!=0):
        res=res*10+n%10
        n=n//10
    return res
    pass


n=int(input())  
rev=reverse(n)
if n==rev:
    print("true")
else:
    print("false")