def mygcd(a,b):
    if(b==0):
        return a
    else:
        return mygcd(b,a%b)
a=60
b=48
x=mygcd(a,b)
print("the gcd of ",a,"and",b,"is",x)