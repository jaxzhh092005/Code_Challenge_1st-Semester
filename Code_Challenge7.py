name = input ("Enter your name:")
buy = input("Did you purchase a grocery today (Yes/No):")
print("======================================")

if buy.lower() == "yes":
    item = input(f"\nHi, {name}, What did you purchase today:")

    price = eval(input("Item Price:"))
    #age = eval(input("Input your age:"))
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