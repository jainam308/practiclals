def count_alphabet_occurrences(filename):
    alphabet_count = {}
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    char = char.lower()
                    if char in alphabet_count:
                        alphabet_count[char] += 1
                    else:
                        alphabet_count[char] = 1
    return alphabet_count

def main():
    filename = input("Enter the filename: ")
    
    try:
        alphabet_occurrences = count_alphabet_occurrences(filename)
        
        print("Alphabet occurrences:")
        for char, count in alphabet_occurrences.items():
            print(f"{char}: {count}")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
