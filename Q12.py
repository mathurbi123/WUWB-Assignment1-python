x = int(input("Enter a number: "))

print("Prime numbers are:", end=" ")
for num in range(2, x + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
