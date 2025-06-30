x = input('Enter no. ')
even = 0
odd = 0
for i in x:
    if int(i)%2==0:
        even +=1
    else:
        odd +=1
print('Even no. are', even)
print('Odd no. are', odd)