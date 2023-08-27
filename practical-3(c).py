
p=int(input("Enter principle amount:-"))
r=int(input("Enter rate of intrest:-")) / 100
t=int(input("Enter time:-"))
n=int(input("Enter N :-"))
simple_interest=(p*r*t)/100
print("the simple intrest is",simple_interest)
compound_interest=p*(1+(r/n*100))**(n*t)
print("The compound interest is ",compound_interest)