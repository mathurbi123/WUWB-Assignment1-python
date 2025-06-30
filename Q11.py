x = int(input('enter a no. '))
for i in range(0, x+1):
    for j in range(1, i+1):
        print(2**(j-1), end='  ')
    print()
    