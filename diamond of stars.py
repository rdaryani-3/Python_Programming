
n = int(input())
for i in range(1, n // 2 + 2):
    print(" " * (n//2 - i+1), end="")
    print("*" * (2 * i - 1), end="")
    print()
for i in range(n // 2, 0, -1):  
    print(" " * (n//2 - i+1), end="")
    print("*" * (2 * i - 1), end="")
    print()