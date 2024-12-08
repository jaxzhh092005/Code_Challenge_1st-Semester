P = eval(input("Enter Prelim Grades:"))
M = eval(input("Enter Midterm Grades:"))
SF = eval(input("Enter Semi-Final Grades:"))
F = eval(input("Enter Final Grades:"))
Q = eval(input("Enter Quiz Grades:"))
PG = eval(input("Enter Project Grades:"))

FG = (P * 0.15)+(M * 0.15)+(SF * 0.15)+(F * 0.15)+(Q * 0.25)+(PG * 0.15)


print(f"The Final Grades is {FG}")


#FG = input("\nENTER FINAL GRADES:")

if 75 <= FG <= 100: 
    print("\nCONGRATULATIONS! YOU PASSED THE COURSE")
   
else: 
    print("\nSORRY YOU FAILED")