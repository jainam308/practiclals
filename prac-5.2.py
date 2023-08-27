l=[]
print(" ENter 10 integer")
for i in range(10):
    x=int(input("Enter an integer:"))
    l.append(x)
for i in range(0,10):
    for j in range(i+1,10):
        print("(", l[i], l[j], end=") ")
