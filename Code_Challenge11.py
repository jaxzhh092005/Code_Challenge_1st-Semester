for h in range(1,6):
    for j in range(h,6):
        print(" ",end=" ")
    for k in range(1,h+1):
        print("*",end=" ")
    for l in range(1,h):
        print("*",end=" ")    
    print()

for m in range(1,5):
    for n in range(1,m+2):
        print(" ", end=" ")
    for o in range(5,m,-1):
       print("*",end=" ")
    for p in range(4,m,-1):
        print("*",end=" ")
    print()