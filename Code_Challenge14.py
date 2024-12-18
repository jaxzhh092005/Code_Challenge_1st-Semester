#CodeChallenge14.py
print("\n----WELCOME TO BANK SIMULATION PROGRAM----")
name = input("ENTER YOUR NAME:")
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