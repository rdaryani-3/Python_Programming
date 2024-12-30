# fahrenhite to cel

# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), 
# you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.


S = int(input())
E = int(input())
W = int(input())

for i in range (S,E+1,W):
    cel = int(5/9 * (i-32))
    print(f"{i} {cel}")