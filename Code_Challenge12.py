for q in range(1,6):
    for r in range(q,6):
        print(" ",end=" ")
    for s in range(1,q+1):
       print("*",end=" ")
    for t in range(1,q+1):
        print("*", end=" ")   
    print()   

for u in range(1,5):
    for v in range(q,6):
        print("         ", end=" ")
    for w in range(q-1,6):
        print("*", end=" ")
    print()