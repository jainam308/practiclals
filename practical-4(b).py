hour=int(input("Enter Number of Hour :- "))
sal=int(input("Enter Money Per Hour :- "))
if(hour<40):
    wage=sal*hour
elif (hour>40):
    ex=hour-40
    es=ex*(1.5*sal) 
    wage=(40*sal)+es    
print(wage)