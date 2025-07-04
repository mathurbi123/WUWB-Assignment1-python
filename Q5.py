x = input('Enter a no. ')
c = len(x)
for i in x:
    b = sum(int(digits)**c for digits in str(x))
print(b)
