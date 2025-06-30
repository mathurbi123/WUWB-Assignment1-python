x = input("Enter a number: ")
is_increasing = True

for i in range(len(x) - 1):
    if x[i] > x[i + 1]:
        is_increasing = False
        break

if is_increasing:
    print("Yes")
else:
    print("No")
