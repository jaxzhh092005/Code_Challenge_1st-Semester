for y in range(1,6):
    for z in range(1,y+1):
        print(" ", end=" ")
    for aa in range(6,y,-1):
        print("*",end=" ")
    print()  