def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2,num):
            if(num%i==0):
                return False
                break
            return True
n=int(input("Enter number:"))
if(is_prime(n)):
    print(n," is prime")
else:
    print(n,"is not prime")        

