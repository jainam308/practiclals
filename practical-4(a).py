year = int(input("Enter Year you want Leap Year Or Not :- "))
if(year%4==0 and year%400==0):
    print("The Year You Entered is Leap Year")
else:
    print("The Year You Entered is not a leap year")     
