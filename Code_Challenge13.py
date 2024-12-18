sum = 0

while True:
    num = eval(input("Enter a number: "))
    if num == 0:
        break
    sum += num

print(f"The total sum is: {sum}")