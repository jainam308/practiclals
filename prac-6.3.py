s=input("enter string:")
x=list(s)
for i in x:
    if(i.isdigit()):
        print(i,'==>',x.count(i))