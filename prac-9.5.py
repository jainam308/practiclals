import numpy as np
import matplotlib.pyplot as plt

def main():
    # Generate random marks for 100 students between 0 and 10
    student_marks = np.random.randint(0, 11, 100)
    
    # Create histogram
    plt.hist(student_marks, bins=11, range=(0, 11), edgecolor='black', alpha=0.7)
    
    plt.xlabel('Marks')
    plt.ylabel('Number of Students')
    plt.title('Histogram of Student Test Marks')
    plt.xticks(np.arange(0, 11))
    plt.yticks(np.arange(0, max(np.bincount(student_marks)) + 1))
    plt.grid(True, axis='y', alpha=0.5)
    
    plt.show()

if __name__ == "__main__":
    main()
