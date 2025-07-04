import math as m
x = int(input('Enter a no. '))
while x >= 10:
    y = m.prod(int(digit) for digit in str(x))

    a = sum(int(d) for d in str(x))
    break
print(y+a)
print((a+y)==x)    
