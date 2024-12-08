name = input("Enter your name:")

amount = eval(input("Enter your amount:"))

THO = amount // 1000
S1 = amount - (1000 * THO)

FH = S1 // 500
S2 = S1 - (500 * FH)


TH = S2 // 200
S3 = S2 - (200 * TH)


OH = S3 // 100
S4 = S3 - (100 * OH)

FP = S4 // 50
S5 = S4 - (50 * FP)

TT = S5 // 20
S6 = S5 - (20 * TT)

TP = S6 // 10
S7 = S6 - (10 * TP)

FP = S7 // 5
S8 = S7 - (5 * FP)

OP = S8 // 1


print("\nHi", name, "your deposit amount breakdown in PH denomination is as follows:")
print(THO, "- 1000")
print(FH, "- 500")
print(TH, "- 200")
print(OH, "- 100")
print(FP, "- 50")
print(TT, "- 20")
print(TP, "- 10")
print(FP, "- 5")
print(OP, "- 1") 



