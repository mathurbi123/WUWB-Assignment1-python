x = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) for digit in str(x))

if x % sum_of_digits == 0:
    print("Yes")
else:
    print("No")
