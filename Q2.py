x = int(input("Enter a no. "))
while x >= 10:
    x = sum(int(digit) for digit in str(x))
print('Output is: ', x)