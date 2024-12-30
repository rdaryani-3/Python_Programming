# difference of AP
#find difference of AP given first 3 numbers

a1, a2, a3 = map(int, input("Enter the first three numbers of an AP, separated by spaces: ").split())

# print("enter 3 numbers of AP")
# a1=int(input())
# a2=int(input())
# a3=int(input())

if ((a2-a1)==(a3-a2)):
    print(a2-a1)
else:
    print("Series isn't a AP")