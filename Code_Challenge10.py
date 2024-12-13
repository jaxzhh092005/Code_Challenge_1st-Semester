for a in range(1,6):
    for b in range(a,6):
        print(" ", end=" ")
    for c in range(1,a+1):
        print("*", end=" ")
    for d in range (1, a+1): 
        print("*", end=" ")  
    print()

for d in range(1,6):
    for e in range(1,d+1):
        print(" ",end=" ")
    for f in range(6,d,-1):
        print("^", end=" ")
    for g in range(6, d,-1):
        print("^",end=" ")
    print()