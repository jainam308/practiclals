def calculate_name_value(name):
    name = name.lower()  # Convert name to lowercase
    value = 0
    
    for char in name:
        if 'a' <= char <= 'z':
            value += ord(char) - ord('a') + 1
    
    return value

def main():
    name = input("Enter a name: ")
    name_value = calculate_name_value(name)
    
    print(f"The numeric value of the name '{name}' is {name_value}.")

if __name__ == "__main__":
    main()
