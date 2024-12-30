# sum even odd

# Write a program to input an integer 'n' and print the sum of all its even digits and the sum of all its odd digits separately.

n = input()
s_odd = 0
s_even = 0

for i in n:
    x = int(i)
    if x %  2 == 0:
        s_even = s_even + x
    else:
        s_odd = s_odd + x

print(s_even, " ",s_odd)
