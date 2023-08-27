for n in range(2,10001):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum =sum+i
    if(n==sum):
        print(n ,"is a perfect number")

