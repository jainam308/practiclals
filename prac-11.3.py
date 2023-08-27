import re

def extract_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        content = file.read()
        numbers = re.findall(r'\d+', content)
    return numbers

def main():
    filename = input("Enter the filename: ")

    try:
        numbers = extract_numbers_from_file(filename)

        if numbers:
            print("Numbers found in the file:")
            for num in numbers:
                print(num)
        else:
            print("No numbers found in the file.")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
