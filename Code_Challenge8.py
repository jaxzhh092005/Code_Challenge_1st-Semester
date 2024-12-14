sum = 0
even = 0
odd = 0

for ff in range(1,11):
    num1= eval(input(f"Input number {ff}:"))
    ev = num1 % 2
    sum +=num1
    if ev == 0:
        even += num1
    else:
        odd += num1
        
print(f"\nThe summation of all number:{sum}")   
print(f"The summation of all even numbers:{even}") 
print(f"The summation of all odd numbers:{odd}")