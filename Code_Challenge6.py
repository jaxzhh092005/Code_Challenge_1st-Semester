name = input("Enter your name:")
age = eval(input("Enter your age:"))


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