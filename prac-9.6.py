# Calculate.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def modulo(x, y):
    if y != 0:
        return x % y
    else:
        return "Cannot divide by zero"

def square(x):
    return x ** 2

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)
#another file
import calculator

def main():
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))

    print("Addition:", calculator.add(x, y))
    print("Subtraction:", calculator.subtract(x, y))
    print("Multiplication:", calculator.multiply(x, y))
    print("Division:", calculator.divide(x, y))
    print("Modulo:", calculator.modulo(x, y))
    print("Square:", calculator.square(x))
    print("Factorial of", x, "is", calculator.factorial(int(x)))

if __name__ == "__main__":
    main()
