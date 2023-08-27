def create_dictionary():
    new_dict = {}
    n = int(input("Enter the number of key-value pairs: "))
    for _ in range(n):
        key = input("Enter key: ")
        value = input("Enter value: ")
        new_dict[key] = value
    return new_dict

def print_dictionary(dictionary):
    print("Dictionary items:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def add_remove(dictionary):
    key = input("Enter key to add/remove: ")
    if key in dictionary:
        del dictionary[key]
        print(f"Key '{key}' removed from dictionary.")
    else:
        value = input(f"Enter value for key '{key}': ")
        dictionary[key] = value
        print(f"Key-value pair '{key}: {value}' added to dictionary.")

def check_key_existence(dictionary):
    key = input("Enter key to check existence: ")
    if key in dictionary:
        print(f"Key '{key}' exists in the dictionary.")
    else:
        print(f"Key '{key}' does not exist in the dictionary.")

def iterate_dictionary(dictionary):
    print("Iterating through the dictionary:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def concatenate_dictionaries(dictionary1, dictionary2):
    concatenated_dict = dictionary1.copy()
    concatenated_dict.update(dictionary2)
    return concatenated_dict

def main():
    dict1 = create_dictionary()

    print_dictionary(dict1)

    add_remove(dict1)
    print_dictionary(dict1)

    check_key_existence(dict1)

    iterate_dictionary(dict1)

    dict2 = create_dictionary()
    concatenated_dict = concatenate_dictionaries(dict1, dict2)
    print("Concatenated dictionaries:")
    print_dictionary(concatenated_dict)

if __name__ == "__main__":
    main()
