import math

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    sqrt_n = math.isqrt(n)
    for i in range(5, sqrt_n + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    
    return True

def main():
    num = int(input("Enter a positive whole number greater than 2: "))
    
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

if __name__ == "__main__":
    main()
