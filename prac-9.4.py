import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

def main():
    x = np.linspace(-5, 5, 100)  # Generate 100 points in the range -5 to 5
    y = relu(x)
    
    plt.plot(x, y, label='ReLU Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of ReLU Function')
    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.show()

if __name__ == "__main__":
    main()
