x = int(input('Enter a no. '))
x_str = str(x)
s = 0
for i in x_str:
    s += int(i)**3
if s==x:
    print("Armstrong no.", s)
else:
    print('Not an amstrong no. ', s)
