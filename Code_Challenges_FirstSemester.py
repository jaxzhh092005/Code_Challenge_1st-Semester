print("\n----CODE CHALLENGE FOR THE FIRST SEMESTER----")
name = input("ENTER YOUR NAME:")

def Code_Challenge1():
    print("\n\t\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t*\t*\t*\t*\t*\t*\t*\n\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t*")

def Code_Challenge2():
    print("\n\t\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t*\t\t   "+"Hi ! "+ name+"\t\t\t*\n\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t*")

def Code_Challenge3():
    num1 = eval(input("\nEnter the first number:"))
    num2 = eval(input("Enter the second number:"))
    
    answer = num1 + num2
    print("\nThe sum of" , num1, "and", num2 , "is", answer)
    answer = num1 - num2
    print("The difference of" , num1, "and", num2 , "is", answer)
    answer = num1 * num2
    print("The product of" , num1, "and", num2, "is", answer)
    answer = num1 / num2
    print("The quotient of", num1, "and", num2, "is", answer)
    answer = num1 ** num2
    print(num1, "exponent by", num2, "is", answer)
    answer = num1 % num2
    print("The remainder of", num1, "and", num2, "is", answer)
    answer = num1 // num2
    print("The floor division of", num1, "and", num2, "is", answer)


def Code_Challenge4():
    amount = eval(input("\nEnter your amount:"))
    
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

def Code_Challenge5():
    P = eval(input("\nEnter Prelim Grades:"))
    M = eval(input("Enter Midterm Grades:"))
    SF = eval(input("Enter Semi-Final Grades:"))
    F = eval(input("Enter Final Grades:"))
    Q = eval(input("Enter Quiz Grades:"))
    PG = eval(input("Enter Project Grades:"))

    FG = (P * 0.15)+(M * 0.15)+(SF * 0.15)+(F * 0.15)+(Q * 0.25)+(PG * 0.15)

    print(f"The Final Grades is {FG}")

    if 75 <= FG <= 100: 
        print("\nCONGRATULATIONS! YOU PASSED THE COURSE")
   
    else: 
        print("\nSORRY YOU FAILED")

def Code_Challenge6():
    age = eval(input("\nEnter your age:"))
    
    if age >= 1 and age <= 8:
        print("\nHi!,", name, "you are considered Toodler")
        
    elif age >= 9 and age <= 14:
       print("\nHi!,", name, "you are considered PreTeen")

    elif age >= 15 and age <= 18:
       print("\nHi!,", name, "you are considered Teenager")

    elif age >= 19 and age <= 27:
       print("\nHi!,", name, "you are considered Early Adulthood")

    elif age >= 28 and age <= 44:
       print("\nHi!,", name, "you are considered Middle Age")

    elif age >= 45 and age <= 59:
       print("\nHi!,", name, "you are considered Past Adulthood")

    elif age >= 60 and age <= 150:
       print("\nHi!,", name, "you are considered Senior")

    else:
       print("\nINVALID AGE")

def Code_Challenge7():
    buy = input("\nDid you purchase a grocery today (Yes/No):")
    print("======================================")

    if buy.lower() == "yes":
        item = input(f"\nHi, {name}, What did you purchase today:")

        price = eval(input("Item Price:"))
        money = eval(input("Payment:"))

        tax = price * 0.123
        final = price + tax
        print(f"Tax Price: {round(final,2)}")

        if price >= 4000:
            discount = (price * 0.038)
            final -= discount
            print(f"Discount Price: {round(discount,2)}")
        

        else:
            print("Discount:0")

            age = eval(input("Input your age:"))
        
            if age >= 60 and age <= 150:
               senior1 = (tax * 0.123)
               final -= senior1
               print(f"Senior Citizen Discount:{round(senior1,2)}")
            
               change = money - final
               print(f"Change:{round(change,2)}")
            
            else:
               print("Sorry not applicable for persons who didn't purchase today")

def Code_Challenge8():
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

def Code_Challenge9():
    for y in range(1,6):
        for z in range(1,y+1):
           print(" ", end=" ")
        for aa in range(6,y,-1):
           print("*",end=" ")
        print()  
    
def Code_Challenge10():
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
    
def Code_Challenge11():
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

def Code_Challenge12():
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

def Code_Challenge13():
    sum = 0

    while True:
       num = eval(input("Enter a number: "))
       if num == 0:
        break
        sum += num
    print(f"The total sum is: {sum}")

def Code_Challenge14():
    print("\n----WELCOME TO BANK SIMULATION PROGRAM----")
    def denominations(amount):
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
        print("\nYOUR DEPOSIT AMOUNT BREAKDOWN IN PH DENOMINATION IS AS FOLLOWS")
        print("1000 -", THO)
        print("500  -",  FH)
        print("200  -",  TH)
        print("100  -",  OH)
        print("50   -",   FP)
        print("20   -",   TT)
        print("10   -",   TP)
        print("5    -",    FP)
        print("1    -",    OP)


    def create_account():
        print("\nCREATING A NEW ACCOUNT...")
        account = {}
        account['balance'] = 0
        return account

    def deposit(account):
        amount = eval(input("ENTER AMOUNT TO DEPOSIT: "))
        denominations(amount)
        account['balance'] += amount
        print(f"DEPOSITED {amount}: PHP." )
        print(f"NEW BALANCE: {account['balance']} PHP")

    def withdraw(account):
        amount = eval(input("ENTER AMOUNT TO WITHDRAW: "))
        if amount > account['balance']:
           print("INSUFFICIENT BALANCE!")
        else:
           account['balance'] -= amount
           print(f"NEW BALANCE: {account['balance']} PHP")

    def check_balance(account):
        print(f"CURRENT BALANCE: {account['balance']} PHP")

    def main():
        account = create_account()
        ideposit = eval(input("ENTER INITIAL DEPOSIT AMOUNT: "))
        denominations(ideposit)
        account['balance'] += ideposit
        print(f"INITIAL DEPOSIT {ideposit} PHP.")
        print(f"CURRENT BALANCE: {account['balance']} PHP")

        while True:
           print("\nOPTIONS:")
           print("1 -- DEPOSIT")
           print("2 -- WITHDRAW")
           print("3 -- CHECK BALANCE")
           print("4 -- EXIT")
           choice = eval(input("CHOOSE AN OPTION: "))

           if choice == 1:
               deposit(account)
           elif choice == 2:
               withdraw(account)
           elif choice == 3:
               check_balance(account)
           elif choice == 4:
               print("\nTHANK YOU FOR USING THE BANK SIMULATION PROGRAM")
               print("EXITING...")
               break
           else:
               print("INVALID OPTION, PLEASE TRY AGAIN")

    if __name__ == "__main__":
       main()


while True:
    print("\nOPTIONS:")
    print("1 -- CODE_CHALLENGE 1")
    print("2 -- CODE_CHALLENGE 2")
    print("3 -- CODE_CHALLENGE 3")
    print("4 -- CODE_CHALLENGE 4")
    print("5 -- CODE_CHALLENGE 5")
    print("6 -- CODE_CHALLENGE 6")
    print("7 -- CODE_CHALLENGE 7")
    print("8 -- CODE_CHALLENGE 8")
    print("9 -- CODE_CHALLENGE 9")
    print("10 -- CODE_CHALLENGE 10")
    print("11 -- CODE_CHALLENGE 11")
    print("12 -- CODE_CHALLENGE 12")
    print("13-- CODE_CHALLENGE 13")
    print("14 -- CODE_CHALLENGE 14")
    print("15 -- EXIT")
    
    
    choice = input("\nCHOOSE AN OPTION: ")
    
    if choice == '1':
        Code_Challenge1()
    elif choice == '2':
        Code_Challenge2()
    elif choice == '3':
        Code_Challenge3()
    elif choice == '4':
        Code_Challenge4()
    elif choice == '5':
        Code_Challenge5()
    elif choice == '6':
        Code_Challenge6()
    elif choice == '7':
        Code_Challenge7()
    elif choice == '8':
        Code_Challenge8()
    elif choice == '9':
        Code_Challenge9()
    elif choice == '10':
        Code_Challenge10()
    elif choice == '11':
        Code_Challenge11()
    elif choice == '12':
        Code_Challenge12()
    elif choice == '13':
        Code_Challenge13()
    elif choice == '14':
        Code_Challenge14()
    elif choice == '15':
        print("\nTHANK YOU FOR USING MY CODES")
        print("EXITING...")
        break
    else:
        print("INVALID OPTION, PLEASE TRY AGAIN")
